from notification import Notification
from slack_service import SlackService

class SlackNotificationAdapter(Notification):
    def __init__(self, login: str, api_key: str, chat_id: str) -> None:
        self.slack_service = SlackService(login, api_key, chat_id)

    def send(self, title: str, message: str) -> None:
        self.slack_service.send_message(title, message)
