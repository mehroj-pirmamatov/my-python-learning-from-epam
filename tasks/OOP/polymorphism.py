class EmailNotification:
    def send(self, message):
        print(f"Email sent: {message}")


class SMSNotification:
    def send(self, message):
        print(f"SMS sent: {message}")


class PushNotification:
    def send(self, message):
        print(f"Push notification sent: {message}")


def notify_user(notification, message):
    notification.send(message)


notifications = [
    EmailNotification(),
    SMSNotification(),
    PushNotification()
]

for notification in notifications:
    notify_user(notification, "Your order has been shipped.")
