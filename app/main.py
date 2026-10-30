
from streamlit.runtime.uploaded_file_manager import UploadedFile
import sys
from pathlib import Path

# Add project root to sys.path so 'db' can be imported
sys.path.append(str(Path(__file__).resolve().parent.parent))

import streamlit as st
from db.database import init_db
from Core.services import Documentservice

st.set_page_config(page_title="Document Management System", layout="wide")

# Initialize database
init_db()

service = Documentservice()

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
    
with tabs[2]:
    #logic for analytics
    pass