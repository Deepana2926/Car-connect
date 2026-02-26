import sys
sys.path.append(r'C:\Users\Rajkumar\Downloads\carconnect')

from util.db_conn_util import get_connection

class UserService:
    def authenticate_admin(self, username, password):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Admin WHERE Username=? AND Password=?", (username, password))
        result = cursor.fetchone()
        conn.close()
        return result

    def authenticate_customer(self, username, password):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Customer WHERE Username=? AND Password=?", (username, password))
        result = cursor.fetchone()
        conn.close()
        return result
