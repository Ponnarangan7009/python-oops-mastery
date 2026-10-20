"""Classes, objects, attributes, and the three common method kinds."""


class TestRun:
    # A class attribute is shared through the class unless an instance shadows it.
    category = "UI automation"

    def __init__(self, name, status):
        # These are instance attributes: each TestRun stores its own values.
        self.name = name
        self.status = status

    # An instance method works with one particular object through self.
    def show_result(self):
        print(f"{self.name}: {self.status} ({self.category})")

    # A class method receives the class as cls. It can create instances
    # or work with class-level information.
    @classmethod
    def from_passed_name(cls, name):
        return cls(name, "PASS")

    # A static method is a related utility. It receives neither self nor cls.
    @staticmethod
    def is_valid_status(status):
        return status in ("PASS", "FAIL", "SKIP")


login_run = TestRun("login", "PASS")
login_run.show_result()

payment_run = TestRun.from_passed_name("payment")
payment_run.show_result()

print(TestRun.is_valid_status("PASS"))
