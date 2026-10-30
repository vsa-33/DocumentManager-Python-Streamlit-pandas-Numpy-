import os
import pymupdf

Thumbnail_path = os.path.join("storage","thumbniles")


class thumbnail:

    def generate_thumbnail(self, pdf_path):
        
        doc = pymupdf.open(pdf_path)
        page = doc.load_page(0)
        pix = page.get_pixmap()
        
        basename = os.path.basename(pdf_path).replace(".pdf",".png")
        
        os.makedirs(Thumbnail_path, exist_ok=True)
        thumbnail_path = os.path.join(Thumbnail_path,basename)
        pix.save(thumbnail_path)
        doc.close()

        return thumbnail_path

    def get_total_pages(self,pdf_path):
        doc = pymupdf.open(pdf_path)
        total_pages = len(doc)
        doc.close()
        return total_pages