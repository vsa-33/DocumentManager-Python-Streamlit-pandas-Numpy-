#streamlit run app/main.py --server.headless true
import os

from datetime import datetime
PDF_STORAGE = os.path.join("storage","pdfs")
class FileManager:

    def save_file(self, uploaded_file):
         timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
         Filename = f'{timestamp}_{uploaded_file.name}'

         filepath = os.path.join(PDF_STORAGE,Filename)

         with open(filepath , "wb") as f:
            f.write(uploaded_file.read())
         return filepath

        