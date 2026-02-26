import sys
sys.path.append(r'C:\Users\Rajkumar\Downloads\carconnect')

from util.db_conn_util import get_connection
from entity.customer import Customer

class CustomerService:
    def get_all_customers(self):
        customers = []
        conn = None
        cursor = None
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Customer")
            rows = cursor.fetchall()
            for row in rows:
                customer = {
                "CustomerID": row[0],
                "FirstName": row[1],
                "LastName": row[2],
                "Email": row[3],
                "PhoneNumber": row[4],
                "Address": row[5],
                "Username": row[6],
                "Password": row[7],
                "RegistrationDate": row[8]
                }
                customers.append(customer)
                return customers
        except Exception as e:
            print("Error fetching customers:", e)
            return []
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def add_customer(self, customer: Customer):
        conn = None
        cursor = None
        try:
            conn = get_connection() 
            cursor = conn.cursor()

            cursor.execute("SELECT ISNULL(MAX(CustomerID), 0) + 1 FROM Customer")
            next_id = cursor.fetchone()[0]

            query = '''
                INSERT INTO Customer (CustomerID, FirstName, LastName, Email, PhoneNumber, Address, Username, Password)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            '''
            cursor.execute(query, (
                next_id,
                customer.first_name,
                customer.last_name,
                customer.email,
                customer.phone_number,
                customer.address,
                customer.username,
                customer.password
            ))

            conn.commit()
            print(f" Customer added successfully with ID: {next_id}")
        except Exception as e:
            print(" Error adding customer:", e)
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
