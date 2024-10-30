from delivery_strategy import DeliveryStrategy

class InternalDeliveryStrategy(DeliveryStrategy):
    def calculate_cost(self, distance: float, weight: float) -> float:
        return distance * 1.25 + weight * 0.4
