from order_page import OrderPage
from date_picker import DatePicker
from time_slot_picker import TimeSlotPicker
from recipient_info import RecipientInfo
from pickup_option import PickupOption
from delivery_mediator import DeliveryMediator

def main():
    mediator = DeliveryMediator(
        date_picker=DatePicker(None),
        time_slot_picker=TimeSlotPicker(None),
        recipient_info=RecipientInfo(None),
        pickup_option=PickupOption(None)
    )

    date_picker = mediator.date_picker
    time_slot_picker = mediator.time_slot_picker
    recipient_info = mediator.recipient_info
    pickup_option = mediator.pickup_option

    date_picker.mediator = mediator
    time_slot_picker.mediator = mediator
    recipient_info.mediator = mediator
    pickup_option.mediator = mediator

    date_picker.select_date("2024-11-01")
    recipient_info.set_different_person(True)
    pickup_option.set_pickup(True)

if __name__ == "__main__":
    main()
