import sys
from datetime import datetime
sys.path.append(r'C:\Users\Rajkumar\Downloads\carconnect')

from service.authentication_service import AuthenticationService
from dao.customer_service import CustomerService
from dao.vehicle_service import VehicleService
from dao.reservation_service import ReservationService
from service.report_generator import ReportGenerator
from entity.customer import Customer
from entity.vehicle import Vehicle
from entity.reservation import Reservation

def show_menu():
    print("\n--- Admin Menu ---")
    print("1. View Customers")
    print("2. View Vehicles")
    print("3. View Reservations")
    print("4. Generate Report")
    print("5. Add Vehicle")
    print("6. Update Vehicle")
    print("7. Delete Vehicle")
    print("8. Make Reservation")
    print("9. Exit")
    print("10.Add Customer")  

if __name__ == "__main__":
    try:
        print("=== Admin Login ===")
        username = input("Username: ")
        password = input("Password: ")

        auth = AuthenticationService()
        if auth.login(username, password):
            print("\nLogin successful!")

            while True:
                show_menu()
                choice = input("Enter your choice (1-10): ")

                if choice == '1':
                    print("\n--- Customers ---")
                    for c in CustomerService().get_all_customers():
                        print(f"ID: {c['CustomerID']} | Name: {c['FirstName']} {c['LastName']} | Email: {c['Email']} | Phone: {c['PhoneNumber']} | Address: {c['Address']} | Username: {c['Username']}")


                elif choice == '2':
                    print("\n--- Vehicles ---")
                    for v in VehicleService().get_all_vehicles():
                        status = "Available" if v.availability else "Not Available"
                        print(f"{v.vehicle_id}. {v.make} {v.model} ({v.year}) - {status}")

                elif choice == '3':
                    print("\n--- Reservations ---")
                    for r in ReservationService().get_all_reservations():
                        print(f"ResID: {r.reservation_id} | Customer: {r.customer_id} | Vehicle: {r.vehicle_id} | ₹{r.total_cost} | {r.status}")

                elif choice == '4':
                    print("\n--- Report ---")
                    ReportGenerator().generate_report()

                elif choice == '5':
                    print("\n--- Add New Vehicle ---")
                    model = input("Model: ")
                    make = input("Make: ")
                    year = int(input("Year: "))
                    color = input("Color: ")
                    reg_number = input("Registration Number: ")
                    availability = int(input("Availability (1 for Yes, 0 for No): "))
                    vehicle = Vehicle(None, model, make, year, color, reg_number, availability)
                    VehicleService().add_vehicle(vehicle)
                    print("Vehicle added successfully!")

                elif choice == '6':
                    print("\n--- Update Vehicle ---")
                    vid = int(input("Enter Vehicle ID to update: "))
                    model = input("New Model: ")
                    make = input("New Make: ")
                    year = int(input("New Year: "))
                    color = input("New Color: ")
                    reg_number = input("New Reg Number: ")
                    availability = int(input("New Availability (1/0): "))
                    vehicle = Vehicle(vid, model, make, year, color, reg_number, availability)
                    VehicleService().update_vehicle(vehicle)
                    print("Vehicle updated successfully!")

                elif choice == '7':
                    print("\n--- Delete Vehicle ---")
                    vid = int(input("Enter Vehicle ID to delete: "))
                    VehicleService().delete_vehicle(vid)
                    print("Vehicle deleted successfully!")

                elif choice == '8':
                    print("\n--- Make Reservation ---")
                    customer_id = int(input("Customer ID: "))
                    vehicle_id = int(input("Vehicle ID: "))
                    start_date = input("Start Date (YYYY-MM-DD HH:MM): ")
                    end_date = input("End Date (YYYY-MM-DD HH:MM): ")
                    total_cost = float(input("Total Cost: "))
                    service = ReservationService()
                    if service.is_vehicle_available(vehicle_id, start_date, end_date):
                        reservation = Reservation(None, customer_id, vehicle_id, start_date, end_date, total_cost, "confirmed")
                        service.make_reservation(reservation)
                        print("Reservation successful")
                    else:
                        print("Vehicle is already booked for the selected dates.")

                elif choice == '9':
                    print("Exit")
                    break

                elif choice == '10':
                    print("\n--- Add New Customer ---")
                    first_name = input("Enter First Name: ")
                    last_name = input("Enter Last Name: ")
                    email = input("Enter Email: ")
                    phone = input("Enter Phone Number: ")
                    address = input("Enter Address: ")
                    username = input("Enter Username: ")
                    password = input("Enter Password: ")
                    customer = Customer(
                        customer_id=None,
                        first_name=first_name,
                        last_name=last_name,
                        email=email,
                        phone_number=phone,
                        address=address,
                        username=username,
                        password=password
                        )
                    customer_service = CustomerService()
                    try:
                        customer_service.add_customer(customer)
                        print("Customer added successfully!")
                    except Exception as e:
                        print(" Error adding customer:", e)

                else:
                    print("Invalid choice. Try again.")

        else:
            print("Invalid credentials. Access denied.")

    except Exception as e:
        print("Error:", e) 

