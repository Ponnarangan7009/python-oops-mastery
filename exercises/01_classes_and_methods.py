"""Exercise: model a support ticket with a class.

Complete the TODOs. The caller at the bottom is provided so you can run
your finished program.
"""


class SupportTicket:
    category = "Customer Support"

    def __init__(self, title, priority):
        # TODO: store title and priority on this instance
        pass

    def show_ticket(self):
        # TODO: print the title, priority, and category
        pass

    @classmethod
    def urgent_ticket(cls, title):
        # TODO: return a ticket with priority "Urgent"
        pass

    @staticmethod
    def is_valid_priority(priority):
        # TODO: return True for Low, Normal, or Urgent; otherwise False
        pass


ticket = SupportTicket("Cannot reset password", "Normal")
ticket.show_ticket()

urgent = SupportTicket.urgent_ticket("Service unavailable")
urgent.show_ticket()

print(SupportTicket.is_valid_priority("Urgent"))
