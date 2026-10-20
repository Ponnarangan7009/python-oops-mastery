"""Exercise: add special methods to a ShoppingCart."""


class ShoppingCart:
    def __init__(self, items):
        self.items = items

    def __str__(self):
        # TODO: return a readable summary of the items
        pass

    def __len__(self):
        # TODO: return the number of items
        pass

    def __eq__(self, other):
        # TODO: compare two ShoppingCart objects by their items
        # Return NotImplemented when other is not a ShoppingCart.
        pass


first = ShoppingCart(["book", "pen"])
second = ShoppingCart(["book", "pen"])

print(first)
print(len(first))
print(first == second)
