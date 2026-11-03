#upload documet functionality 

# we will process uploaded---> create thumbnile---> images as same name of pdf

from datetime import datetime


from db.repository import Documetrepos
from Core.file_manager import FileManager
from Core.thumbnile import thumbnail
from Core.pdfreader import PDFReader



class Documentservice:
    def __init__(self):

        self.repo = Documetrepos()
        self.file_manager = FileManager()
        self.thumbnail_generator = thumbnail()
        self.reader = PDFReader()

    def Uploadfile(self,uploaded_file,tags,description,lecture_date=None):
        doc =[]
        #save the file

        file_path = self.file_manager.save_file(uploaded_file)

        thumbnail_path = self.thumbnail_generator.generate_thumbnail(file_path)

        total_pages = self.thumbnail_generator.get_total_pages(file_path)

        self.reader.get_imgaes(file_path)

        upload_date = datetime.now().strftime("%Y-%m-%d")

        

        doc.append(file_path.name)
        doc.append(file_path)
        doc.append(thumbnail_path)
        doc.append(tags)
        doc.append(description)
        doc.append(upload_date)
        doc.append(lecture_date)
        doc.append(total_pages)
    
    
    def search_documents(self, tag=None, date=None):

        return self.repo.search_documents(tag,date)

        


       

        #genrate thumnile
        #get total pages
        #convert to images
        #create upload dates and other varibales
        #save it to database table
        #self.repo.add_documnet(doc)
