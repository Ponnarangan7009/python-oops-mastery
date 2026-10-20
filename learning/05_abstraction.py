"""Abstraction with ABC: require child classes to implement an operation."""

from abc import ABC, abstractmethod


class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        """Concrete payment types must implement this operation."""
        pass


class CardPayment(PaymentMethod):
    def __init__(self, last_four_digits):
        self.last_four_digits = last_four_digits

    def pay(self, amount):
        print(f"Paid {amount} by card ending in {self.last_four_digits}.")


class CashPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paid {amount} in cash.")


def process_payment(payment_method, amount):
    payment_method.pay(amount)


process_payment(CardPayment("1234"), 250)
process_payment(CashPayment(), 250)
