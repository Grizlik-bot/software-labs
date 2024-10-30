from abc import ABC, abstractmethod

class EntityUpdateProcessor(ABC):
    def update_entity(self):
        entity = self.get_entity()
        if self.validate_data(entity):
            self.save_data(entity)
            self.send_response(200, "Success", self.get_additional_response_data())
        else:
            self.handle_validation_failure(entity)
            self.send_response(400, "Validation failed", None)

    @abstractmethod
    def get_entity(self):
        pass

    @abstractmethod
    def validate_data(self, entity) -> bool:
        pass

    @abstractmethod
    def save_data(self, entity):
        pass

    def handle_validation_failure(self, entity):
        pass

    def get_additional_response_data(self):
        return None

    def send_response(self, status_code: int, status: str, additional_data):
        print(f"Status Code: {status_code}, Status: {status}, Data: {additional_data}")
