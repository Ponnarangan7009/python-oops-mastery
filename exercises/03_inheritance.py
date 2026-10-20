"""Exercise: extend a base class using inheritance and super()."""


class Appliance:
    def __init__(self, brand):
        # TODO: store the brand
        pass

    def describe(self):
        # TODO: print "Brand: <brand>"
        pass


class WashingMachine(Appliance):
    def __init__(self, brand, capacity_kg):
        # TODO: initialize the parent part with super()
        # TODO: store capacity_kg
        pass

    def describe(self):
        # TODO: call the parent's describe() and print the capacity
        pass


washer = WashingMachine("Bosch", 8)
washer.describe()
