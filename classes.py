# class Point():
# def __init__(self, x, y):
# self.x = x
# self.y = y


# p = Point(150, 8)
# print(p.x)
# print(p.y)

# this will print 150 & 8

class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)


flight = Flight(3)

people = ["Jon", "Ron", "Harry", "Kramer", "Gerald", "Anthony"]
for person in people:
    if flight.add_passenger(person):
        print(f"Added {person} to flight successfully")
    else:
        print(f"No available seats for {person}")
