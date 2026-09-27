# OOP PILLAR - INHERITENCE: PRACTICE


class Notification:
    def send(self):
        print("Sending notification")


class EmailNotification(Notification):
    def send(self):
        print("Sending email")


email = Notification()
email.send()


class Camera:
    def take_photo(self):
        print("Photo captured")


class GPS:
    def get_location(self):
        print("Location found")


class SmartDevice(Camera, GPS):
    pass


device = SmartDevice()

device.take_photo()
device.get_location()


# Base Class (Hierarchical Parent)
class Vehicle:
    def __init__(self, name):
        self.name = name

    def start_engine(self):
        print(f"{self.name}'s engine is running.")


# Child Class 1 (Inherits from Vehicle)
class Car(Vehicle):
    def drive(self):
        print(f"{self.name} is driving on roads.")


# Child Class 2 (Inherits from Vehicle)
class Boat(Vehicle):
    def sail(self):
        print(f"{self.name} is sailing on water.")


# Hybrid Class (Multiple inheritance from Car and Boat)
class AmphibiousVehicle(Car, Boat):
    def transition_mode(self):
        print(f"{self.name} is switching between land and water!")


# --- Demonstration ---
# Create an instance of the hybrid class
amphi_car = AmphibiousVehicle("AquaCar")

# 1. Access method from the ultimate grandparent (Vehicle)
amphi_car.start_engine()

# 2. Access method from Parent 1 (Car)
amphi_car.drive()

# 3. Access method from Parent 2 (Boat)
amphi_car.sail()

# 4. Access its own method
amphi_car.transition_mode()


class X:
    def show(self):
        print("X")


class Y(X):
    pass


class Z(X):
    pass


class Final(Y, Z):
    pass


print(Final.mro())
