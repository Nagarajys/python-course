# Problem 1: Private Attribute + Constructor + Getter
"""Create a class called BankAccount.

Your class should have:

A constructor that receives the account balance.
Store the balance in a private attribute called __balance.
Create a method called get_balance() that returns the private balance.
Create one object with balance 5000.
Print the balance using get_balance()."""


class bankaccount:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance


acc = bankaccount(5000)
print(acc.get_balance())


"""Problem 2/30 — Encapsulation

Create a class called Mobile.

Requirements:

Constructor should receive price.
Store price as a private attribute __price.
Create a setter method called set_price().
set_price() should change the private price.
Create one object with price 20000.
Change its price to 25000 using the setter.
Print the final price using a getter."""


class mobile:
    def __init__(self, price):
        self.__price = price

    def get_price(self):
        return self.__price

    def set_price(self, price):
        if price > 0:
            self.__price = price


vivo = mobile(20000)
print(vivo.get_price())
vivo.set_price(25000)
print(vivo.get_price())


"""Problem 3/30 — Encapsulation

Create a class called Employee.

Requirements:

Constructor should receive:
name
salary
Store both as private attributes:
__name
__salary
Create a getter for the name.
Create a getter for the salary.
Create a setter for the salary.
Salary should be changed only if the new salary is greater than 0.
Create two Employee objects with different names and salaries.
Change the salary of one employee using the setter.
Print both employees' names and final salaries using getters."""


class employe:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    def get_name(self):
        return self.__name

    def get_salary(self):
        return self.__salary

    def set_salary(self, new_salary):
        if new_salary > 0:
            self.__salary = new_salary


emp1 = employe("rahulla", 20000)
emp2 = employe("nagaraj", 250000)
print(emp1.get_name())
print(emp1.get_salary())
emp2.set_salary(300000)
print(emp2.get_name())
print(emp2.get_salary())


"""Problem 4/30 — Encapsulation

 private data + validation a little more.

Create a class called Product.

Requirements:

Constructor receives:
name
price
Store both as private attributes:
__name
__price
Create getters for both.
Create a setter for price.
The setter should allow the price to change only if the new price is between 100 and 10000.
If the price is outside that range, do not change the old price.

Create one product:

name = "Laptop"
price = 5000
Try changing price to 50.
Print the final price."""


class product:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        if new_price >= 100 and new_price <= 10000:
            self.__price = new_price
        else:
            self.__price = (
                self.__price
            )  # this is not necesarry , we can do nothing also


laptop = product("asus", 80000)
print(laptop.get_name())
laptop.set_price(999)
print(laptop.get_price())


""" Problem 5/30 — Encapsulation
private data + controlled operation, without a setter.

Create a class Wallet.

Requirements:
Store it as private:
Create get_balance() to read the balance.
Create add_money(amount):
If amount > 0, add it to the private balance.
Otherwise, don't change the balance.
Create one wallet with balance = 1000.
Add 500.
Print the final balance."""


class wallet:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def add_money(self, amount):
        if amount > 0:
            self.__balance = self.__balance + amount


money = wallet(1000)
print(money.get_balance())
money.add_money(500)
print(money.get_balance())


""" Problem 6/30 — Encapsulation

withdrawal + validation + balance protection.

Create a class called ATM.

Requirements:

Constructor receives balance.
Store it as private attribute __balance.
Create get_balance() to return the balance.
Create withdraw(amount):
amount must be greater than 0.
Amount must not be greater than the current balance.
If both conditions are valid, subtract the amount.
Otherwise, don't change the balance.
Create an ATM object with balance 10000.
Withdraw 3000.
Print the final balance."""


class ATM:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance = self.__balance - amount
        else:
            print("balance  is not available ")


atm1 = ATM(10000)
print(atm1.get_balance())
atm1.withdraw(3000)
print(atm1.get_balance())

"""Problem 7/30 — Encapsulation

Now let's introduce two private attributes + independent setters.

Create a class called UserProfile.

Requirements:

Constructor receives:
username
age

Store both as private:

__username
__age
Create:
get_username()
get_age()
Create:
set_username(new_username)
set_age(new_age)
Username should change only if it is not empty.
Age should change only if it is between 18 and 60.

Create one object:

username = "nagaraj"
age = 18
Change username to "nagaraj_ys".
Change age to 20.
Print the final username and age using getters."""


class userprofile:
    def __init__(self, username, age):
        self.__username = username
        self.__age = age

    def get_name(self):
        return self.__username

    def get_age(self):
        return self.__age

    def set_name(self, new_username):
        if new_username != "":
            self.__username = new_username

    def set_age(self, new_age):
        if new_age >= 18 and new_age <= 60:
            self.__age = new_age


object = userprofile("nagaraj", 18)
object.set_name("nagaraj ys")
object.set_age(20)
print(object.get_name())
print(object.get_age())


"""Problem 8/30 — Encapsulation
Now let's make the validation a little more interesting.
Create a class called LibraryBook.
Requirements:
Constructor receives:
title
available
Store both as private attributes:
__title
__available
Create get_title() and get_available().
Create a method borrow_book().
A book can be borrowed only if it is currently available.
If available:
change availability to False.
If already borrowed:
don't change anything.

Create one book:

title = "Python Basics"
available = True
Print availability.
Call borrow_book().
Print availability again."""


class library:
    def __init__(self, title, available):
        self.__title = title
        self.__available = available

    def get_title(self):
        return self.__title

    def get_available(self):
        return self.__available

    def borrow_book(self):
        if self.__available == True:
            self.__available = False


book = library("rich dad", True)
print(book.get_title())
print(book.get_available())
book.borrow_book()
print(book.get_available())

# problem 9:
"""Now we're adding a calculated value + private data pattern.

Create a class called Product.

Requirements:

Constructor receives:
name
price
quantity

Store all three as private attributes:

__name
__price
__quantity
Create getters for name, price, and quantity.
Create a method get_total_cost().
get_total_cost() should calculate:
price × quantity
Create one product:
name = "Keyboard"
price = 1500
quantity = 3
Print:
Product name
Total cost"""


class order:
    def __init__(self, item, price, quantity):
        self.__item = item
        self.__price = price
        self.__quantity = quantity

    def get_item(self):
        return self.__item

    def get_price(self):
        return self.__price

    def get_quantity(self):
        return self.__quantity

    def get_total_amount(self):
        return self.__price * self.__quantity


summary = order("headphones", 2000, 5)
print(summary.get_item())
summary.get_total_amount
print(summary.get_total_amount())


""" Problem 10/30 — Encapsulation

pattern: private data + validation + calculated method together, but with a completely new scenario.

Create a class called ElectricityBill.

Requirements:

Constructor receives:
customer
units

Store both as private attributes:

__customer
__units
Create a getter for customer.
Create a getter for units.

Create a method:

calculate_bill()
Billing rules:
If units ≤ 100 → bill = units × 5
If units > 100 → bill = units × 7

Create one object:

customer = "Nagaraj"
units = 150
Print customer name and calculated bill."""


class electricitybill:
    def __init__(self, customer, units):
        self.__customer = customer
        self.__units = units

    def get_customer(self):
        return self.__customer

    def get_units(self):
        return self.__units

    def calculate_bill(self):
        if self.__units <= 100:
            bill = self.__units * 5
        else:
            bill = self.__units * 7
        return bill


customer = electricitybill("nagarajys", 150)
print(customer.get_customer())
customer.calculate_bill
print(customer.calculate_bill())

""" Problem 11/30 — Encapsulation
multiple objects + private data + comparison.

Create a class called Player.

Requirements:

Constructor receives:
name
score

Store them as private:

__name
__score
Create getters for both.
Create 3 player objects with different scores.
Using the private data through getters, determine which player has the highest score.
Print the winner's name and score."""


class player:
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score


p1 = player("nagaraj", 100)
p2 = player("nishanth", 87)
p3 = player("rahulla", 28)
highest = p1
if p2.get_score() > highest.get_score():
    highest = p2
if p3.get_score() > highest.get_score():
    highest = p3
print(highest.get_name())
print(highest.get_score())


class BankCard:
    def __init__(self, card_holder, balance, limit):
        self.__card_holder = card_holder
        self.__balance = balance
        self.__limit = limit

    def get_card_holder(self):
        return self.__card_holder

    def get_balance(self):
        return self.__balance

    def get_limit(self):
        return self.__limit

    def set_limit(self, new_limit):
        if new_limit > 0:
            self.__limit = new_limit

    def spend(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance = self.__balance - amount

    def add_money(self, amount):
        if amount > 0:
            self.__balance = self.__balance + amount


card = BankCard("Nagaraj", 10000, 50000)

print(card.get_card_holder())
print(card.get_balance())
print(card.get_limit())

card.spend(3000)
card.add_money(2000)
card.set_limit(60000)

print(card.get_balance())
print(card.get_limit())


"""Problem 14/30 — Abstraction

Scenario: Payment System

Create an abstract class called Payment.

Requirements:

Import ABC and abstractmethod.
Payment should inherit from ABC.
Create an abstract method pay(self, amount).
Create a child class UPI that inherits from Payment.
UPI must implement pay().
When pay(500) is called, print:
Paid 500 using UPI
Create a UPI object and call pay(500)."""


from abc import ABC, abstractmethod


class payment(ABC):  # what must done - pay()
    @abstractmethod  # what should child have told by parent class
    def pay(self, amount):
        pass


class upi(payment):  # how it is done - upi s pay()
    def pay(self, amount):  # how does upi do it , its own implementation
        print("sutejh paid", amount, "using upi")


obj = upi()
obj.pay(1000)

"""             PAYMENT
          (ABC / Parent)
                |
          "You MUST have
             pay()"
                |
        @abstractmethod
                |
       -------------------
       |                 |
      UPI           CreditCard
       |                 |
   pay() method      pay() method
       |                 |
   HOW UPI pays     HOW Card pays"""


"""ABC → abstract parent/base class
@abstractmethod → child must implement this method
pass → parent gives no implementation
class UPI(Payment) → UPI is child of Payment
Parent = WHAT, Child = HOW"""


""" Problem 15/30 — Abstraction

Ippo one abstract class + one child class + abstract method implementation

Scenario: Animal

Create an abstract class called Animal.

Requirements:

Import ABC and abstractmethod.
Animal should inherit from ABC.

Create an abstract method:

make_sound(self)
Create a child class Dog that inherits from Animal.
Dog must implement make_sound().

Inside Dog's method, print:

Dog barks
Create a Dog object and call make_sound()."""

from abc import ABC, abstractmethod


class animal(ABC):
    @abstractmethod
    def make_sound(self):  # PARENT CLASS TELING TO CHILD CLASS
        pass


class dog(animal):
    def make_sound(self):
        print("dog barks")  # child class implimenting thiss


doggy = dog()
doggy.make_sound()


"""Problem 16/30 

Q16. Write a Python program to demonstrate Abstraction using an Abstract Base Class.

Requirements:

a) Create an abstract class Notification using ABC.

b) Define an abstract method send(self, message) using @abstractmethod.

c) Create two derived classes:

EmailNotification
SMSNotification

d) Implement the send() method in both derived classes with appropriate messages.

e) Create objects of both derived classes and call the send() method with "Hello"."""


from abc import ABC, abstractmethod


class notification(ABC):
    @abstractmethod
    def send(self, message):
        pass


class emailnotification(notification):
    def send(self, message):
        print("email sent:", message)


class smsnotification(notification):
    def send(self, message):
        print("sms sent:", message)


emn = emailnotification()
smn = smsnotification()
emn.send("hello")
smn.send("hello")


""" Problem 17/30 — Abstraction

Q17. Write a Python program to demonstrate abstraction using an abstract class Shape.

Requirements:

a) Create an abstract class Shape using ABC.

b) Define an abstract method area(self) using @abstractmethod.

c) Create two derived classes:

Circle
Rectangle

d) Circle should accept radius through its constructor and implement area() using:


e) Rectangle should accept length and breadth through its constructor and implement area() using:


f) Create objects of both classes.

g) Call area() for both objects and display the results."""


from abc import ABC, abstractmethod


class shape(ABC):
    @abstractmethod
    def area(self):
        pass


class circle(shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print("area of circle:", 3.14 * self.radius * self.radius)


class rectangle(shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        print("area of rectangle:", 3.14 * self.length * self.breadth)


cir = circle(5)
rect = rectangle(10, 4)
cir.area()
rect.area()


"""Q18. Write a Python program to demonstrate abstraction using an abstract class Employee.

Requirements:

a) Create an abstract class Employee using ABC.

b) Define an abstract method:

calculate_salary(self)

c) Create two derived classes:

FullTimeEmployee
PartTimeEmployee

d) FullTimeEmployee should accept monthly_salary through its constructor and implement calculate_salary().

e) PartTimeEmployee should accept hours and rate_per_hour through its constructor and implement calculate_salary().

f) Create one object of each class.

g) Call calculate_salary() for both objects."""

from abc import ABC, abstractmethod


class employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass


class FullTimeEmploye(employee):
    def __init__(self, monthly_salary):
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        print("Full time salary", self.monthly_salary)


class PartTimeEmploye(employee):
    def __init__(self, hours, rate_per_hour):
        self.hours = hours
        self.rate_per_hour = rate_per_hour

    def calculate_salary(self):
        print("part time salary", self.hours * self.rate_per_hour)


ft = FullTimeEmploye(50000)
pt = PartTimeEmploye(80, 300)

ft.calculate_salary()
pt.calculate_salary()


"""Q19. Write a Python program to demonstrate abstraction using an abstract class Appliance.

Requirements:

a) Create an abstract class Appliance using ABC.

b) Define an abstract method:

turn_on(self)

c) Create two derived classes:

Fan
WashingMachine

d) Implement turn_on() differently in both classes.

e) Create an object of each class.

f) Call turn_on() for both objects."""

from abc import ABC, abstractmethod


class appliance(ABC):
    @abstractmethod
    def turn_on(self):
        pass


class fan(appliance):
    def turn_on(self):
        print("fan is turned on")


class washingMechine(appliance):
    def turn_on(self):
        print("washing mechine is running")


objfan = fan()
objwash = washingMechine()
objfan.turn_on()
objwash.turn_on()


"""Q20. Write a Python program to demonstrate that an abstract class cannot be instantiated directly.

Requirements:

a) Create an abstract class Vehicle using ABC.

b) Define an abstract method:

start(self)

c) Create a child class Car that inherits from Vehicle.

d) Implement start() inside Car and print:

Car started

e) Create a Car object and call start().

f) Also attempt to create an object of the abstract class Vehicle directly."""


from abc import ABC, abstractmethod


class vehical(ABC):
    @abstractmethod
    def start(self):
        pass


class car(vehical):
    def start(
        self,
    ):  # You cannot directly create an object of an ABSTRACT class that still has abstract methods.
        print("car is started")


carobj = car()
carobj.start()


"""Q21. Write a Python program to demonstrate an abstract class containing both an abstract method and a normal method.

Requirements:

a) Create an abstract class Bank using ABC.

b) Define an abstract method:

calculate_interest(self)

c) Define a normal method:

display_bank_name(self)

It should print:

ABC Bank

d) Create a child class SavingsAccount that inherits from Bank.

e) Implement calculate_interest() in SavingsAccount.

Use:

Principal = 10000
Interest rate = 5%

Calculate interest using:

$$ Interest = \frac{Principal \times Rate}{100} $$

f) Create a SavingsAccount object.

g) Call both:

display_bank_name()
calculate_interest()"""


from abc import ABC, abstractmethod


class bank(ABC):
    @abstractmethod
    def calculate_interest(self):
        pass

    def display_bank_name(self):
        print("ABC bank")


class savings_account(bank):
    def __init__(self, principle, rate):
        self.principle = principle
        self.rate = rate

    def calculate_interest(self):
        print("intrest:", (self.principle * self.rate) / 100)


saveacc = savings_account(10000, 5)
saveacc.calculate_interest()
saveacc.display_bank_name()


"""Q22. Write a Python program to demonstrate abstraction for calculating the salary of different types of workers.

Requirements:

a) Create an abstract class Worker using ABC.

b) Define an abstract method:

calculate_payment(self)

c) Create two derived classes:

HourlyWorker
FixedWorker

d) HourlyWorker should accept:

hours
rate

through its constructor.

Its calculate_payment() should calculate:

hours × rate

e) FixedWorker should accept monthly_payment through its constructor.

Its calculate_payment() should return the fixed monthly payment.

f) Create one object of each class using:

HourlyWorker → hours = 120, rate = 250
FixedWorker → monthly_payment = 40000

g) Call calculate_payment() for both objects."""

from abc import ABC, abstractmethod


class Worker(ABC):

    @abstractmethod
    def calculate_payment(self):
        pass


class HourlyWorker(Worker):

    def __init__(self, hours, rate):
        self.hours = hours
        self.rate = rate

    def calculate_payment(self):
        print("Hourly Worker Payment:", self.hours * self.rate)


class FixedWorker(Worker):

    def __init__(self, monthly_payment):
        self.monthly_payment = monthly_payment

    def calculate_payment(self):
        print("Fixed Worker Payment:", self.monthly_payment)


hw = HourlyWorker(120, 250)
fw = FixedWorker(40000)

hw.calculate_payment()
fw.calculate_payment()
