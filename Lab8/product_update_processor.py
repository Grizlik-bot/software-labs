from entity_update_processor import EntityUpdateProcessor

class ProductUpdateProcessor(EntityUpdateProcessor):
    def get_entity(self):
        return Product()

    def validate_data(self, entity) -> bool:
        return True

    def save_data(self, entity):
        print("Saving product data")

    def handle_validation_failure(self, entity):
        print("Sending a notification to the administrator via messenger")
