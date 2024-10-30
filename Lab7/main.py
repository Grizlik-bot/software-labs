from delivery_context import DeliveryContext
from pickup_strategy import PickupStrategy
from external_delivery_strategy import ExternalDeliveryStrategy
from internal_delivery_strategy import InternalDeliveryStrategy

def main():
    context = DeliveryContext()

    context.set_delivery_method(PickupStrategy())
    print("ֳ�� ����������:", context.calculate_delivery_cost(10, 5))

    context.set_delivery_method(ExternalDeliveryStrategy())
    print("ֳ�� �������� ��������� �������:", context.calculate_delivery_cost(10, 5))

    context.set_delivery_method(InternalDeliveryStrategy())
    print("ֳ�� �������� ������� �������:", context.calculate_delivery_cost(10, 5))

if __name__ == "__main__":
    main()
