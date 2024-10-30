from product_update_processor import ProductUpdateProcessor
from user_update_processor import UserUpdateProcessor
from order_update_processor import OrderUpdateProcessor

if __name__ == "__main__":
    product_processor = ProductUpdateProcessor()
    product_processor.update_entity()

    user_processor = UserUpdateProcessor()
    user_processor.update_entity()

    order_processor = OrderUpdateProcessor()
    order_processor.update_entity()
