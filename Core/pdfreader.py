from sympy import Matrix
from PIL.ImagePalette import load
from genericpath import exists
import pymupdf
import os 

class PDFReader:
    def get_imgaes(self,pdf_path):
        doc = pymupdf.open(pdf_path)

        folder_name = os.path.basename(pdf_path).replace(".pdf", "")
        output_dir = os.path.join("storgae", "pdfs" , folder_name)

        if not os.path.exists(output_dir):
            os.mkdir(output_dir)

        images_path = []

        for i in len(doc):
            page = doc.load_page(i)
            pymupdf.Matrix(2,2)

            pix = page.get_pixmap(matrix=Matrix)
            img_path = os.path.join(output_dir,f'Page_{i}.png')
            pix.save(img_path)
            images_path.append(img_path)
        doc.close()



