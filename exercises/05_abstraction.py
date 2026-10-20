"""Exercise: create concrete notification types from an abstract base."""

from abc import ABC, abstractmethod


class Notification(ABC):
    @abstractmethod
    def send(self, message):
        # The abstract method defines the required behavior.
        pass


class PushNotification(Notification):
    def send(self, message):
        # TODO: print "Push: <message>"
        pass


class SlackNotification(Notification):
    def send(self, message):
        # TODO: print "Slack: <message>"
        pass


def send_notification(notification, message):
    notification.send(message)


send_notification(PushNotification(), "Build completed")
send_notification(SlackNotification(), "Review needed")
