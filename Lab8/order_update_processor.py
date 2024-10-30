from entity_update_processor import EntityUpdateProcessor

class OrderUpdateProcessor(EntityUpdateProcessor):
    def get_entity(self):
        return Order()

    def validate_data(self, entity) -> bool:
        return True

    def save_data(self, entity):
        print("Saving order data")

    def get_additional_response_data(self):
        return {"Order": "JSON Representation"}

    def handle_validation_failure(self, entity):
        print("Handling validation error for order")
