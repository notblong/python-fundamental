class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, passenger):
        if self.is_open_seat() == False:
            return False

        self.passengers.append(passenger)
        return True

    def is_open_seat(self):
        return self.capacity - len(self.passengers)


flight = Flight(2)
passengers = ["Mr White", "Ms Green", "Mrs Blue"]

for p in passengers:
    add_success = flight.add_passenger(p)
    if add_success:
        print(f"Added {p} success.")
    else:
        print(f"Cannot add {p} due to out of capacity.")
