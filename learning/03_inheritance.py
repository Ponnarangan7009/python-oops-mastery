"""Inheritance, overriding, super(), multiple inheritance, and MRO."""


class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def introduce(self):
        print(f"Employee: {self.name} (ID: {self.employee_id})")


class Manager(Employee):
    def __init__(self, name, employee_id, team_size):
        # Reuse Employee's initialization instead of duplicating it.
        super().__init__(name, employee_id)
        self.team_size = team_size

    # Override the inherited method and extend its behavior.
    def introduce(self):
        super().introduce()
        print(f"Manages {self.team_size} people")


class Camera:
    def take_photo(self):
        print("Taking a photo.")


class Phone:
    def make_call(self):
        print("Making a call.")


class CameraPhone(Camera, Phone):
    pass


lead = Manager("Asha", "E104", 5)
lead.introduce()

device = CameraPhone()
device.take_photo()
device.make_call()

print(isinstance(lead, Employee))       # True: Manager is an Employee.
print(issubclass(Manager, Employee))     # True
print(CameraPhone.mro())                # The method lookup order.
