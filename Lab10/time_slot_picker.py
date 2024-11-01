from mediator import Mediator

class TimeSlotPicker:
    def __init__(self, mediator: Mediator):
        self.mediator = mediator
        self.available_time_slots = []

    def update_time_slots(self, date):
        # Update list of available time slots based on date
        self.mediator.notify(self, "time_slots_updated")