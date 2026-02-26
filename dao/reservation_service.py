import sys
sys.path.append(r'C:\Users\Rajkumar\Downloads\carconnect')

from util.db_conn_util import get_connection
from entity.reservation import Reservation

class ReservationService:
    def get_all_reservations(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Reservation")
        rows = cursor.fetchall()
        reservations = []
        for row in rows:
            reservations.append(Reservation(*row))
        conn.close()
        return reservations
    
    def is_vehicle_available(self, vehicle_id, start, end):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM Reservation
        WHERE VehicleID = ?
        AND (
            (StartDate BETWEEN ? AND ?) OR
            (EndDate BETWEEN ? AND ?)
        )
        AND Status = 'confirmed'
        """, (vehicle_id, start, end, start, end))
        result = cursor.fetchone()
        conn.close()
        return result is None

    def make_reservation(self, reservation):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO Reservation (CustomerID, VehicleID, StartDate, EndDate, TotalCost, Status)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (reservation.customer_id, reservation.vehicle_id, reservation.start_date, reservation.end_date, reservation.total_cost, reservation.status))
        conn.commit()
        conn.close()


