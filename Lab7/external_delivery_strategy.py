from delivery_strategy import DeliveryStrategy

class ExternalDeliveryStrategy(DeliveryStrategy):
    def calculate_cost(self, distance: float, weight: float) -> float:
        return distance * 2.0 + weight * 0.5
