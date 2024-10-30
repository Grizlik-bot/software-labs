from entity_update_processor import EntityUpdateProcessor

class UserUpdateProcessor(EntityUpdateProcessor):
    def get_entity(self):
        return User()

    def validate_data(self, entity) -> bool:
        return True

    def save_data(self, entity):
        print("Saving user data (email cannot be changed)")

    def handle_validation_failure(self, entity):
        print("Handling validation error for user")
