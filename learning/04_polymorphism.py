"""Polymorphism: one operation can work with different object types."""


class EmailAlert:
    def send(self, message):
        print(f"Email alert: {message}")


class SMSAlert:
    def send(self, message):
        print(f"SMS alert: {message}")


def notify(alert, message):
    # This function relies on behavior (send), not a specific class name.
    alert.send(message)


notify(EmailAlert(), "Build completed")
notify(SMSAlert(), "Build failed")
