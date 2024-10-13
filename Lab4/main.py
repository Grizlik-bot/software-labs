from email_notification import EmailNotification
from slack_notification_adapter import SlackNotificationAdapter
from sms_notification_adapter import SmsNotificationAdapter

def main():
    #email
    email_notification = EmailNotification("admin@example.com")
    email_notification.send("Hello", "No")

    #Slack
    slack_notification = SlackNotificationAdapter("user_login", "api_key", "chat123")
    slack_notification.send("Cool", "Release")

    #SMS
    sms_notification = SmsNotificationAdapter("1234567890", "MyCompany")
    sms_notification.send("Error", "Throw an error")

if __name__ == "__main__":
    main()
