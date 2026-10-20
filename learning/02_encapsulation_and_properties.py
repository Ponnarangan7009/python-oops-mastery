"""Encapsulation conventions, name mangling, and properties."""


class BankAccount:
    def __init__(self, owner, opening_balance):
        self.owner = owner
        self.__internal_id = f"ACCOUNT-{self.owner.upper()}"
        # A leading underscore communicates: internal implementation detail.
        self._balance = 0
        self.balance = opening_balance  # invokes the property setter

    @property
    def balance(self):
        """Read the balance through the public attribute-like interface."""
        return self._balance

    @balance.setter
    def balance(self, new_balance):
        if not isinstance(new_balance, (int, float)):
            raise TypeError("Balance must be a number.")
        if new_balance < 0:
            raise ValueError("Balance cannot be negative.")
        self._balance = new_balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be greater than zero.")
        self._balance += amount

    def account_reference(self):
        # Double underscore triggers name mangling; it is not security.
        return self.__internal_id



account = BankAccount("Asha", 100)
account.deposit(25)
print(account.balance)
account.balance = 200
print(account.balance)
print(account.account_reference())

# Python name-mangles a double-underscore attribute. This works, but normal
# application code should use account_reference() instead of relying on it.
print(account._BankAccount__internal_id)
