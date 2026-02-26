import sys
sys.path.append(r'C:\Users\Rajkumar\Downloads\carconnect')

import pyodbc
def get_connection():
    return pyodbc.connect(
        r"Driver={SQL Server};Server=LAPTOP-C3S3TQVJ\SQLEXPRESS;Database=CARCONNECT;Trusted_Connection=yes;"
    )

