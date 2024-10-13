from notification import Notification
from sms_service import SmsService

class SmsNotificationAdapter(Notification):
    def __init__(self, phone: str, sender: str) -> None:
        self.sms_service = SmsService(phone, sender)

    def send(self, title: str, message: str) -> None:
        self.sms_service.send_sms(title, message)
