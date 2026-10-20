"""Custom exceptions give application-specific errors meaningful names."""


class InsufficientFundsError(Exception):
    """Raised when a withdrawal is greater than the available balance."""


class Wallet:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError("Withdrawal exceeds wallet balance.")
        self.balance -= amount
        return self.balance


wallet = Wallet(50)

try:
    wallet.withdraw(75)
except InsufficientFundsError as error:
    print(f"Could not complete withdrawal: {error}")
