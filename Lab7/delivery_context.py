from delivery_strategy import DeliveryStrategy

class DeliveryContext:
    def __init__(self):
        self._strategy: DeliveryStrategy = None

    def set_delivery_method(self, strategy: DeliveryStrategy):
        self._strategy = strategy

    def calculate_delivery_cost(self, distance: float, weight: float) -> float:
        if not self._strategy:
            raise ValueError("Спосіб доставки не встановлено")
        return self._strategy.calculate_cost(distance, weight)
