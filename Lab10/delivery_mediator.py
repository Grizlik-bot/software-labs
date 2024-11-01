from mediator import Mediator

class DeliveryMediator(Mediator):
    def __init__(self, date_picker, time_slot_picker, recipient_info, pickup_option):
        self.date_picker = date_picker
        self.time_slot_picker = time_slot_picker
        self.recipient_info = recipient_info
        self.pickup_option = pickup_option

    def notify(self, sender, event):
        if event == "date_selected":
            self.time_slot_picker.update_time_slots(self.date_picker.selected_date)
        elif event == "different_person_set":
            self.recipient_info.update_required_fields()
        elif event == "pickup_set":
            if self.pickup_option.is_pickup:
                self.disable_delivery_options()
            else:
                self.enable_delivery_options()

    def disable_delivery_options(self):
        # Disabling shipping related items
        pass

    def enable_delivery_options(self):
        # Enabling shipping related items
        pass
