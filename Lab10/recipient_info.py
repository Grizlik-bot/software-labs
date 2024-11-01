from mediator import Mediator

class RecipientInfo:
    def __init__(self, mediator: Mediator):
        self.mediator = mediator
        self.is_different_person = False
        self.recipient_name = ""
        self.recipient_phone = ""

    def set_different_person(self, is_different):
        self.is_different_person = is_different
        self.mediator.notify(self, "different_person_set")

    def update_required_fields(self):
        # Updateing required fields depending on "other recipient" state
        pass
