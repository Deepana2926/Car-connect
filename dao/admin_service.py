import sys
sys.path.append(r'C:\Users\Rajkumar\Downloads\carconnect')


import pyodbc

class AdminService:
    def authenticate(self,username, password):
        try:
            conn = pyodbc.connect(
                r"Driver={SQL Server};Server=LAPTOP-C3S3TQVJ\SQLEXPRESS;Database=CARCONNECT;Trusted_Connection=yes;"
            )
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Admin")
            rows = cursor.fetchall()
            conn.close()
            return rows  # return list of all admins for display/test
        except Exception as e:
            print("Database connection error:", e)
            return None



