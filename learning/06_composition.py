"""Composition: one object stores and uses another object."""


class Battery:
    def power_on(self):
        print("Battery supplies power.")


class Flashlight:
    def __init__(self, battery):
        # Store a reference to the Battery object passed by the caller.
        self.battery = battery

    def turn_on(self):
        # Delegate battery-related work to the Battery object.
        self.battery.power_on()
        print("Flashlight is on.")


battery = Battery()
flashlight = Flashlight(battery)
flashlight.turn_on()

# The relationship is "a Flashlight has a Battery", not "is a Battery".
