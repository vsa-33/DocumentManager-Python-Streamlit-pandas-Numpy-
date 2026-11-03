
from streamlit.runtime.state import session_state
from streamlit.runtime.uploaded_file_manager import UploadedFile
import sys
from pathlib import Path

# Add project root to sys.path so 'db' can be imported
sys.path.append(str(Path(__file__).resolve().parent.parent))

import streamlit as st
from db.database import init_db
from Core import services

st.set_page_config(page_title="Document Management System", layout="wide")
if "selected_doc" not in st.session_state:
    st.session_state.selected_doc = None

if "current_page" not in st.session_state:
    st.session_state.current_page = 0


if "Search"  not in st.session_state:
    st.session_state.Search=[]

if "reader_mode" not in st.session_state:
    st.session_state.reader_mode=False

# Initialize database
init_db()

service = services.Documentservice()

st.title("Document PDF Management System")
st.divider()

tabs = st.tabs(["Upload","Serarch&View","Analytics"])

with tabs[0]:
    st.header("Upload PDF")
    uploaded_file = st.file_uploader("Upload PDF", type="PDF")
    tags = st.text_input("Tags(comma seprated)")
    description = st.text_area("Description")
    lecture_date = st.date_input("Leacture Date(Optional)", value=None)
    #Upload_date = st.date_input("Upload_date(Optional)", input=None)

    if st.button("Upload"):
        if uploaded_file:
            service.Uploadfile(uploaded_file,tags,description,lecture_date)
        else:
            st.error("Please Upload a valid file")
        #and tags and description:


with tabs[1]:
    st.header("Search&View")

    col1,col2 = st.columns(2)

    with col1:
        search_tag = st.text_input("search by tags")
    
    with col2:
        search_date = st.date_input("search by date" , value=None)
    
    if st.button("Search"):
        st.session_state.Search = service.search_documents(
            tag=search_tag if search_tag else None,
            date =str(search_date) if search_date else None
            )
    
    results = st.session_state.Search

    if results and not st.session_state.reader_mode:
        st.subheader(f'Results: {len(results)} documnets')
        container = st.container(height=600)
        with container:
                for doc in results:
                    col1,col2 = st.columns([1,3])
                    with col1:
                        if doc.thumbnail_path:
                            st.image(doc.thumbnail_path, width=120)
            
                    with col2:
                        st.write(f'{doc.name}')
                        st.write(f'Tgas: {doc.tags}')
                        st.write(f'Description: {doc.description}')
                        st.write(f'Lecture Date: {doc.lecture_date}')

                        if st.button("Open",key=f'open_{doc.id}'):
                            st.session_state.selected_doc = doc
                            st.session_state.current_page = 0
                            st.session_state.reader_mode = True
                            st.rerun()
    
    if st.session_state.reader_mode and st.session_state.selected_doc:
        st.write("Reader Mode Active")



    
with tabs[2]:
    #logic for analytics
    pass