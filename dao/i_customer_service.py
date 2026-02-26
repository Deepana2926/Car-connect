from abc import ABC, abstractmethod

class ICustomerService(ABC):
    @abstractmethod
    def get_all_customers(self): pass

