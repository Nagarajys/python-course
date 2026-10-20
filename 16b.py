# ISP:
# a class should have the methods which needed to it dont force other extra methods:
from abc import ABC, abstractmethod


class Teaching(ABC):
    @abstractmethod
    def teach(self):
        pass


class Coding(ABC):
    @abstractmethod
    def write_code(self):
        pass


class Cleaning(ABC):
    @abstractmethod
    def clean(self):
        pass


class Teacher(Teaching):
    def teach(self):
        print("teacher will teach")


class Programmer(Coding):
    def write_code(self):
        print("programmer writing python code")


class Cleaner(Cleaning):
    def clean(self):
        print("cleaning a floor")


p1 = Teacher()
p2 = Programmer()
p3 = Cleaner()
p1.teach()
p2.write_code()
p3.clean()


# ISP 2ND QUESTION::
from abc import ABC, abstractmethod


class Smart_Phone(ABC):
    @abstractmethod
    def call(self):
        pass

    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def capture(self):
        pass


class Music_Playlist(ABC):
    @abstractmethod
    def play(self):
        pass


class Digital_Camera(ABC):
    @abstractmethod
    def capture(self):
        pass


class Smart_phone_user(Smart_Phone):
    def call(self):
        print("make call to google ceo")

    def play(self):
        print("play tabahi")

    def capture(self):
        print("captured animal photoooo")


class Music_Player(Music_Playlist):
    def play(self):
        print("PLAY DREAM FUNKK FHAAA")


class Photographer(Digital_Camera):
    def capture(self):
        print("CAPTURE MY PHOTOTOOTOOTTOT")


phone = Smart_phone_user()
music = Music_Player()
Photo = Photographer()
phone.call()
phone.play()
phone.capture()
music.play()
phone.capture()


##HOMEWORKKKK
# 1.SRP
class Book:
    def __init__(self, book_name, author, rate):
        self.book_name = book_name
        self.author = author
        self.rate = rate


class book_information:
    def book_details(self, book):
        print(f"book name is:{book.book_name}")
        print(f"author name is:{book.author}")
        print(f"rate is:{book.rate}")


books = Book("rich dad", "nagaraj", 4999)
printer = book_information()
printer.book_details(books)


# 2.OCP HW:
class Billing_system:
    def calculate_tax(self, price):
        pass


class Food(Billing_system):
    def calculate_tax(self, price):
        total = price * 9.5
        print(total)


class Electronics(Billing_system):
    def calculate_tax(self, price):
        total = price * 12.5
        print(total)


food = Food()
electronics = Electronics()
food.calculate_tax(259)
electronics.calculate_tax(999)


# 3.LSP....hw

from abc import ABC, abstractmethod


# 1. Define a clear base class interface
class Vehicle(ABC):
    @abstractmethod
    def move(self) -> None:
        pass


# 2. Subclasses implement the exact same interface
class Bike(Vehicle):
    def move(self) -> None:
        print("Moving on the road.")


class Boat(Vehicle):
    def move(self) -> None:
        print("Moving through the water.")


# 3. A client function that demonstrates LSP
# This function accepts ANY Vehicle and can call .move() blindly
def start_journey(vehicle: Vehicle):
    vehicle.move()  # Works perfectly regardless of the subclass passed


# Testing the substitution
biker = Bike()
boater = Boat()

start_journey(biker)  # Output: Moving on the road.
start_journey(boater)  # Output: Moving through the water.
