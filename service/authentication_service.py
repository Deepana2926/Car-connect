import sys
sys.path.append(r'C:\Users\Rajkumar\Downloads\carconnect')


from dao.admin_service import AdminService
from exceptions.authentication_exception import AuthenticationException


class AuthenticationService:
    def __init__(self):
        self.admin_service = AdminService()

    def login(self, username, password):
        if not self.admin_service.authenticate(username, password):
            raise AuthenticationException("Invalid credentials")
        return True
