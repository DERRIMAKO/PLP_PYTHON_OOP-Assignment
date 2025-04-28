# Activity 2: Polymorphism Challenge!

# Define a base class for vehicles
class Vehicle:
    """Base class representing a vehicle."""
    def move(self):
        return "The vehicle is moving."

# Define subclasses with different move behaviors
class Car(Vehicle):
    def move(self):
        return "The car is driving on the road."

class Plane(Vehicle):
    def move(self):
        return "The plane is flying in the air."

class Boat(Vehicle):
    def move(self):
        return "The boat is sailing on water."

# Demonstrate polymorphism
vehicles = [Car(), Plane(), Boat()]

for vehicle in vehicles:
    print(vehicle.move())  # Each vehicle calls its own move() method
