# OOP ADVANCED PROBLEMS:
"""Problem 16/30 — Mixed 4 Pillars: Online Course System

Build an Online Course Management System using all 4 OOP pillars:

Requirements

Create a base class User that stores:

name
email

Then create a class Student that inherits from User.

The student should have:

a private course enrollment status
a method to enroll in a course
a method to display enrollment status

Create an abstract class Course with an abstract method:

calculate_fee()

Create two child classes:

RegularCourse
PremiumCourse

Each course must calculate its fee differently.

Finally, create multiple course objects and use polymorphism to calculate their fees without using if/elif to identify the course type.
"""

from abc import ABC, abstractmethod


class user:
    def __init__(self, name, email):
        self.name = name
        self.email = email


class Student(user):
    def __init__(self, name, email):
        super().__init__(name, email)
        self.__enrolled = False

    def enroll(self):
        self.__enrolled = True
        print(self.name, "enrollled sucessfully")

    def show_status(self):
        if self.__enrolled:
            print("enrolled status:", "enrolled")
        else:
            print("enrollled status:", "not enrolled")


class course(ABC):
    @abstractmethod
    def calculate_fee(self) -> int:  # returns integer
        pass


class RegularCourse(course):
    def calculate_fee(self) -> int:
        fee = 500
        return fee


class PremiumCourse(course):
    def calculate_fee(self) -> int:
        fee = 3000
        return fee


student_details = Student("nagaraj", "nagaraj.kondlur@gamil.com")

student_details.enroll()
student_details.show_status()

courses = [RegularCourse(), PremiumCourse()]

for python in courses:
    print("course fees:", python.calculate_fee())


# Problem 17/30 — Food Delivery Order System

"""Build a Food Delivery Order System using all 4 OOP pillars.

Requirements

Create a base class Order that stores:

order_id
customer_name

Create a child class CustomerOrder that inherits from Order.

The order should contain a private delivery status.

Create an abstract class Delivery with an abstract method:

calculate_delivery_charge(distance)

Create these child classes:

NormalDelivery
ExpressDelivery
PriorityDelivery

Each must calculate the delivery charge differently.

Your program must:
Create one customer order.
Change its delivery status using a method.
Display the delivery status.
Create all three delivery objects.
Store them in one list.
Use one for loop to calculate their charges.
Do not use if/elif to identify the delivery type.
Use all 4 pillars."""

from abc import ABC, abstractmethod


class Order:
    def __init__(self, order_id, customer_name):
        self.order_id = order_id
        self.customer_name = customer_name


class customer_order(Order):
    def __init__(self, order_id, customer_name):
        super().__init__(order_id, customer_name)
        self.__delivery_status = False  # dont execute this before executing below block

    def calculate_delivery_charge(self):
        self.__delivery_status = True
        print("ORDER_ID:", self.order_id)
        print("CUSTMER NAME:", self.customer_name)

    def show_status(self):
        if self.__delivery_status:
            print("DELIVERY STATUS: DELIVERED")
        else:
            print("DELIVERY STATUS: NOT DELIVERED")


class Delivery(ABC):
    @abstractmethod
    def calculate_deliver_charge(self, distance):
        pass


class Normal_delivery(Delivery):
    def calculate_deliver_charge(self, distance):
        print("NORMAL DELIVERY CHARGE = ", distance * 20, "RUPEES")


class Express_delivery(Delivery):
    def calculate_deliver_charge(self, distance):
        print("EXPRESS DELIVERY  CHARGE = ", distance * 40, "RUPEES")


class Priority_delivery(Delivery):
    def calculate_deliver_charge(self, distance):
        print("PREMIUM DELIVERY CHARGE = ", distance * 60, "RUPEES")


customer_details = customer_order("KA14100", "NAGARAJ")
customer_details.calculate_delivery_charge()
customer_details.show_status()
deliveries = [Normal_delivery(), Express_delivery(), Priority_delivery()]
kms = [10, 25, 8]
for delivery, km in zip(deliveries, kms):
    delivery.calculate_deliver_charge(km)


# Problem 18/30 — Online Banking Transaction System

"""Build an Online Banking Transaction System using all 4 OOP pillars.

Requirements
Create a base class BankAccount
Store account_number
Store account_holder
Create a child class CustomerAccount
Inherit from BankAccount
Maintain a private balance
Provide methods to:
deposit money
withdraw money
display balance

Create an abstract class Transaction

Create abstract method:
process(amount)

Create 3 child classes:

UPITransaction
CardTransaction
NetBankingTransaction

Each must override process(amount) and calculate/display its own transaction fee.

Create one list containing all 3 transaction objects.
Create a separate list of transaction amounts.
Use one for loop + zip() to process them.
Do not use if/elif to identify transaction type."""

from abc import ABC, abstractmethod


class Bankaccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder


class Customer_account(Bankaccount):
    def __init__(self, account_number, account_holder):
        super().__init__(account_number, account_holder)
        self.__balance = 0

    def deposit_money(self, amount):
        self.__balance += amount
        print("AMOUNT DEPOSITED:", amount)

    def withdraw_money(self, amount):
        self.__balance -= amount
        print("AMOUNT WITHDRAWN:", amount)

    def display_balance(self):
        print("CURRENT BALANCE:", self.__balance)


class Transaction(ABC):
    @abstractmethod
    def process(self, amount):
        pass


class UPITransaction(Transaction):
    def process(self, amount):
        fee = amount * 2 / 100
        final_amount = amount + fee
        print("UPI TRANSACTION")
        print("AMOUNT:", amount)
        print("FEE:", fee)
        print("FINAL AMOUNT:", final_amount)


class CardTransaction(Transaction):
    def process(self, amount):
        fee = amount * 3 / 100
        final_amount = amount + fee
        print("CARD TRANSACTION")
        print("AMOUNT:", amount)
        print("FEE:", fee)
        print("FINAL AMOUNT:", final_amount)


class NetBankingTransaction(Transaction):
    def process(self, amount):
        fee = amount * 1 / 100
        final_amount = amount + fee
        print("NET BANKING TRANSACTION")
        print("AMOUNT:", amount)
        print("FEE:", fee)
        print("FINAL AMOUNT:", final_amount)


holder_details = Customer_account(3730, "NAGARAJ YS")

holder_details.deposit_money(25000)
holder_details.withdraw_money(5000)
holder_details.display_balance()


transaction_objects = [UPITransaction(), CardTransaction(), NetBankingTransaction()]

transaction_amounts = [5000, 8000, 10000]

for obj, amt in zip(transaction_objects, transaction_amounts):
    obj.process(amt)
