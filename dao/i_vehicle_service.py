from abc import ABC, abstractmethod

class IVehicleService(ABC):
    @abstractmethod
    def get_all_vehicles(self): pass

