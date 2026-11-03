
from streamlit.proto import ArrowNamedDataSet_pb2
from pymupdf import Document
from db.database import connection

class Documetrepos:
    

    def add_documnet(self,doc):
        conn = connection()
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO documents(
        Filename,
        Path,
        Thumbnail_path,
        Tags,
        Description,
        Upload_date,
        Lecture_Date,
        Total_Pages
        )
        VALUES(?,?,?,?,?,?,?,?)
        """,(
        doc[0],
        doc[1],
        doc[2],
        doc[3],
        doc[4],
        doc[5],
        doc[6],
        doc[7]
        
        ))
        conn.commit()
        conn.close()


    def search_documnet(self,tag= None, date=None):
        conn = connection()
        cursor = conn.cursor()

        query = "select * from documents"

        conditions=[]
        param = []

        if tag:
            conditions.append("tags like ?")
            param.append(f'%{tag}%')
        
        if date:
            conditions.append(" Lecture_Date = ?")
            param.append(f'%{date}%')

        if conditions:
            query += " WHERE " + " OR " .join(conditions)

        cursor.execute(query,param)
        rows = cursor.fetchall()
        cursor.close()
        return[ Document(*row) for row in rows]

        