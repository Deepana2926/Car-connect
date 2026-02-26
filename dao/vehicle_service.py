import sys
sys.path.append(r'C:\Users\Rajkumar\Downloads\carconnect')

from util.db_conn_util import get_connection
from entity.vehicle import Vehicle

class VehicleService:
    def get_all_vehicles(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Vehicle")
        rows = cursor.fetchall()
        vehicles = []
        for row in rows:
            vehicles.append(Vehicle(*row))
        conn.close()
        return vehicles

    def add_vehicle(self, vehicle):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Vehicle (Model, Make, Year, Color, RegistrationNumber, Availability)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            vehicle.model,
            vehicle.make,
            vehicle.year,
            vehicle.color,
            vehicle.registration_number,
            vehicle.availability
        ))
        conn.commit()
        conn.close()

    def update_vehicle(self, vehicle):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE Vehicle
            SET Model = ?, Make = ?, Year = ?, Color = ?, RegistrationNumber = ?, Availability = ?
            WHERE VehicleID = ?
        """, (
            vehicle.model,
            vehicle.make,
            vehicle.year,
            vehicle.color,
            vehicle.reg_number,
            vehicle.availability,
            vehicle.vehicle_id
        ))
        conn.commit()
        conn.close()

    def delete_vehicle(self, vehicle_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Vehicle WHERE VehicleID = ?", (vehicle_id,))
        conn.commit()
        conn.close()
