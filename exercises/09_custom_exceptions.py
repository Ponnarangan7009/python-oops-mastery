"""Exercise: define and raise a custom exception for an invalid booking."""


# TODO: define BookingLimitError that inherits from Exception.


class EventBooking:
    def __init__(self, available_seats):
        self.available_seats = available_seats

    def book(self, seats):
        # TODO: if seats exceeds available_seats, raise BookingLimitError
        # Otherwise subtract seats and return the remaining seat count.
        pass


booking = EventBooking(3)

try:
    print(booking.book(2))
    print(booking.book(2))
except Exception as error:
    print(f"Booking could not be completed: {error}")
