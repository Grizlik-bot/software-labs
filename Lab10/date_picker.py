from mediator import Mediator

class DatePicker:
    def __init__(self, mediator: Mediator):
        self.mediator = mediator
        self.selected_date = None

    def select_date(self, date):
        self.selected_date = date
        self.mediator.notify(self, "date_selected")
