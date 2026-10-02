"""INHERITANCE — PROBLEM 1/30

 Pattern: Single Inheritance

Create a parent class LibraryItem.

Parent class requirements:
title attribute
show_title() method
Child class:

Create Book that inherits from LibraryItem.

Book should have:

author attribute
show_book() method

Create a Book object with:

Title: Python Programming
Author: Mark"""


class libraryitem:
    def __init__(self, title):
        self.title = title

    def show_title(self):
        print("title:", self.title)


class Book(libraryitem):
    def __init__(self, title, author):
        super().__init__(title)
        self.author = author

    def show_book(self):
        self.show_title()
        print("author:", self.author)


book = Book("python programing", "nagaraj")
book.show_book()
# super() parent object/data ಅನ್ನು "bring" ಮಾಡೋದಿಲ್ಲ — parent classನ method/constructor ಅನ್ನು call ಮಾಡುತ್ತದೆ.


# Pattern: Multilevel Inheritance
class employee:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print("name:", self.name)


class devoloper(employee):
    def __init__(self, name, language):
        super().__init__(name)
        self.language = language

    def show_language(self):
        print("language:", self.language)


class AI_devoloper(devoloper):
    def __init__(self, name, language, details):
        super().__init__(name, language)
        self.details = details

    def show_details(self):
        self.show_name()
        self.show_language()
        print("Specalization:", self.details)


ai_era = AI_devoloper("karthik", "java", "applied AI")
ai_era.show_details()


# Problem 3/30 — Multiple Inheritance
class camera:
    def take_camera(self):
        print("photo captured")


class GPS:
    def get_location(self):
        print("location: bengaluru")


class smartPhone(camera, GPS):
    def show_device(self):
        self.take_camera()
        self.get_location()
        print("device:" "smartPhone")


phone = smartPhone()
phone.show_device()