from mediator import Mediator

class PickupOption:
    def __init__(self, mediator: Mediator):
        self.mediator = mediator
        self.is_pickup = False

    def set_pickup(self, is_pickup):
        self.is_pickup = is_pickup
        self.mediator.notify(self, "pickup_set")
