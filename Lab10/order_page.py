from mediator import Mediator

class OrderPage:
    def __init__(self, mediator: Mediator):
        self.mediator = mediator
        self.date_picker = None
        self.time_slot_picker = None
        self.recipient_info = None
        self.pickup_option = None

    def set_date_picker(self, date_picker):
        self.date_picker = date_picker

    def set_time_slot_picker(self, time_slot_picker):
        self.time_slot_picker = time_slot_picker

    def set_recipient_info(self, recipient_info):
        self.recipient_info = recipient_info

    def set_pickup_option(self, pickup_option):
        self.pickup_option = pickup_option

    def update_delivery_options(self):
        self.mediator.notify(self, "update_delivery_options")
