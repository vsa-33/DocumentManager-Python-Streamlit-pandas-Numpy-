
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
