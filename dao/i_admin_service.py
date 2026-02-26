from abc import ABC, abstractmethod

class IAdminService(ABC):
    @abstractmethod
    def authenticate(self, username, password): pass
