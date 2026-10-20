"""Exercise: validate a thermostat's target temperature.

Complete the TODOs. The public property should be named target_temperature;
store its value in _target_temperature. Reject values outside 10..30.
"""


class Thermostat:
    def __init__(self, target_temperature):
        # TODO: initialize target_temperature using the property
        pass

    @property
    def target_temperature(self):
        # TODO: return the stored temperature
        pass

    @target_temperature.setter
    def target_temperature(self, new_temperature):
        # TODO: require a number from 10 through 30, inclusive
        # Use TypeError for a non-number and ValueError for out-of-range values.
        pass


thermostat = Thermostat(22)
print(thermostat.target_temperature)

thermostat.target_temperature = 25
print(thermostat.target_temperature)
