from delivery_strategy import DeliveryStrategy

class PickupStrategy(DeliveryStrategy):
    def calculate_cost(self, distance: float, weight: float) -> float:
        return 0.0
