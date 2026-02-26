import sys
import unittest
from datetime import datetime

sys.path.append(r'C:\Users\Rajkumar\Downloads\carconnect')

from service.authentication_service import AuthenticationService
from dao.customer_service import CustomerService
from dao.vehicle_service import VehicleService
from entity.customer import Customer
from entity.vehicle import Vehicle


class TestCarConnectSystem(unittest.TestCase):

    def setUp(self):
        self.auth_service = AuthenticationService()
        self.customer_service = CustomerService()
        self.vehicle_service = VehicleService()

    def test_admin_login_valid(self):
        result = self.auth_service.login("deepu", "dg123")
        self.assertTrue(result, "Valid admin login should return True")

    def test_admin_login_invalid(self):
        result = self.auth_service.login("invaliduser", "wrongpass")
        self.assertFalse(result, "Invalid admin login should return False")

    def test_add_new_customer(self):
        customer = Customer(
            customer_id=None,  #auto-generate
            first_name="Navin",
            last_name="K",
            email="Navin@gmail.com",
            phone_number="8508266764",
            address="chennai",
            username="Navin",
            password="@123",
            registration_date=None  #default date
            )
        result = self.customer_service.add_customer(customer)
        self.assertIsNone(result, "CustomerService should not return anything if successful")  

    def test_add_vehicle(self):
        vehicle = Vehicle(
            vehicle_id=None,
            model="BMW",
            make="i6",
            year=2025,
            color="Blue",
            registration_number="KN1234NN10",
            availability=1
        )
        result = self.vehicle_service.add_vehicle(vehicle)
        self.assertIsNone(result, "VehicleService should not return anything if successful") 

if __name__ == '__main__':
    unittest.main()
