import sys
sys.path.append(r'C:\Users\Rajkumar\Downloads\carconnect')

import pyodbc
from dao.reservation_service import ReservationService

class ReportGenerator:
    def generate_report(self):
        service = ReservationService()
        reservations = service.get_all_reservations()
        print("Reservation Report")
        for r in reservations:
            print(f"ResID: {r.reservation_id}, Customer: {r.customer_id}, Vehicle: {r.vehicle_id}, Status: {r.status}")

def generate_revenue_report(self):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(TotalCost) FROM Reservation WHERE Status='confirmed'")
    revenue = cursor.fetchone()[0]
    print(f"Total Revenue from Confirmed Reservations: ₹{revenue}")
    conn.close()

def most_booked_vehicle(self):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT TOP 1 VehicleID, COUNT(*) AS Bookings
        FROM Reservation
        WHERE Status='confirmed'
        GROUP BY VehicleID
        ORDER BY Bookings DESC
    """)
    result = cursor.fetchone()
    print(f"Most Booked Vehicle ID: {result[0]} - Bookings: {result[1]}")
    conn.close()
