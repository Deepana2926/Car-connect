from abc import ABC, abstractmethod

class IReservationService(ABC):
    @abstractmethod
    def get_all_reservations(self): pass
