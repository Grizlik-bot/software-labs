from abc import ABC, abstractmethod

class DeliveryStrategy(ABC):
    @abstractmethod
    def calculate_cost(self, distance: float, weight: float) -> float:
        pass
