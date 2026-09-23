# PROBLEMS ON ABSTRACTION AND ENCAPSULATION (PILLARS OF OOP)
from abc import ABC, abstractmethod


class ATM(ABC):
    @abstractmethod
    def withdraw(self, amount):
        pass


class savingsatm(ATM):
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance = self.__balance - amount
            print("withdraw:", amount)
            print("remaining balance :", self.__balance)
        else:
            print("invalid withdrawl")


obj = savingsatm(10000)
obj.withdraw(3000)
obj.withdraw(8000)


"""🔥 Problem 24/30 — Exam Style: Vehicle Rental System

Write a Python program for a Vehicle Rental System using both Encapsulation and Abstraction.

Requirements

1. Abstract class: Vehicle

Create an abstract method:

calculate_rent(self, days)

2. Child class: Car

The Car class should have private attributes:

__model
__price_per_day

Use a constructor to initialize them.

3. Getter methods

Create:

get_model(self)
get_price(self)

to access the private data.

4. Implement calculate_rent()

Total rent:

price_per_day × days

Return the calculated amount.

5. Validation

If days <= 0, print:

Invalid number of days

Otherwise return the total rent."""

from abc import ABC, abstractmethod


class vehical(ABC):
    @abstractmethod
    def calculate_rent(self, days):
        pass


class car(vehical):
    def __init__(self, model, price_per_day):
        self.__model = model
        self.__price_per_day = price_per_day

    def get_model(self):
        return self.__model

    def get_price_per_day(self):
        return self.__price_per_day

    def calculate_rent(self, days):
        print("model:", self.__model)
        print("price per day:", self.__price_per_day)
        if days <= 0:
            print("invalid number of days")
        else:
            print("total rent:", self.__price_per_day * days)


summary = car("THAR ROXX", 2000)
summary.calculate_rent(5)


"""🔥 Q25/30 — Hospital Management System

Write a Python program using both Encapsulation and Abstraction.

Requirements:

Create an abstract class Hospital.

Create an abstract method:

calculate_bill(self)
Create child class Patient.
Patient must have these private attributes:
__name
__days
__price_per_day
Create a constructor to initialize them.
Create getters:
get_name()
get_days()

calculate_bill() should calculate:

days × price_per_day

If days <= 0, print:

Invalid number of days
Otherwise print the patient's name and total bill."""

from abc import ABC, abstractmethod


class hospital(ABC):
    @abstractmethod
    def calculate_bill(self):
        pass


class patient(hospital):
    def __init__(self, name, days, price_per_day):
        self.__name = name
        self.__days = days
        self.__price_per_day = price_per_day

    def get_name(self):
        return self.__name

    def get_days(self):
        return self.__days

    def calculate_bill(self):
        print("name:", self.__name)
        print("days:", self.__days)
        print("price_per_days:", self.__price_per_day)
        if self.__days <= 0:
            print("invalid number of days")
        else:
            print("total bill:", self.__days * self.__price_per_day)


description = patient("nagaraj", 2, 3000)
description.calculate_bill()

"""Q26/30 — E-Commerce Payment System — HARD

Write a Python program using Encapsulation + Abstraction + Multiple Child Classes.

Requirements:

Create abstract class Payment.
Create abstract method:
make_payment(self, amount)
Create two child classes:
CreditCardPayment
UPIPayment
CreditCardPayment must have private:
__card_holder
__balance
UPIPayment must have private:
__upi_id
__balance
Both classes must implement make_payment().
Payment should happen only if:
amount > 0
AND
amount <= balance
If successful:
payment successful
remaining balance: ...
Otherwise:
payment failed
Create objects for both payment methods and perform a payment."""

from abc import ABC, abstractmethod


class payment(ABC):
    @abstractmethod
    def make_payment(self, amount):
        pass


class credit_card_payment(payment):
    def __init__(self, card_holder, balance):
        self.__card_holder = card_holder
        self.__balance = balance

    def get_card_holder(self):
        return self.__card_holder

    def get_balance(self):
        return self.__balance

    def make_payment(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance = self.__balance - amount
            print("card_holder_name:", self.__card_holder)
            print("UPI payment:", amount)
            print("remaining balance:", self.__balance)
        else:
            print("payment failed")


class UPI_payment(payment):
    def __init__(self, upi_id, balance):
        self.__upi_id = upi_id
        self.__balance = balance

    def get_upi_id(self):
        return self.__upi_id

    def get_balance(self):
        return self.__balance

    def make_payment(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance = self.__balance - amount
            print("upi id", self.__upi_id)
            print("UPI payment:", amount)
            print("remaining balance:", self.__balance)
        else:
            print("upi payment failed")


phonepay = credit_card_payment("nagaraj", 30000)
upi = UPI_payment("rahulla", 15000)
phonepay.make_payment(5000)
upi.make_payment(5000)
upi.make_payment(10000)

""" Q27 — Banking Loan Approval System

Write a Python program using Abstraction + Encapsulation + Multiple Classes + Conditional Decision Logic.

Requirements

Create an abstract class:

Loan

with abstract method:

check_eligibility(self)
Class 1 — HomeLoan

Private attributes:

__applicant
__salary
__credit_score
__existing_loan
Class 2 — EducationLoan

Private attributes:

__applicant
__salary
__credit_score
__student_age
Eligibility rules
HomeLoan

Loan is eligible only if ALL conditions are true:

salary >= 50000
credit_score >= 700
existing_loan == False

If eligible:

Home Loan Approved

Otherwise:

Home Loan Rejected
EducationLoan

Loan is eligible only if ALL conditions are true:

salary >= 25000
credit_score >= 650
student_age <= 25

If eligible:

Education Loan Approved

Otherwise:

Education Loan Rejected"""


from abc import ABC, abstractmethod


class loan(ABC):
    @abstractmethod
    def check_eligibility(self):
        pass


class HomeLoan(loan):
    def __init__(self, applicant, salary, credit_score, existing_loan):
        self.__applicant = applicant
        self.__salary = salary
        self.__credit_score = credit_score
        self.__existing_loan = existing_loan

    def check_eligibility(self):
        if (
            self.__salary >= 50000
            and self.__credit_score >= 750
            and self.__existing_loan == False
        ):
            print("homeloan approved")
        else:
            print("home loan rejected")


class EducationLoan(loan):
    def __init__(self, applicant, salary, credit_score, student_age):
        self.__applicant = applicant
        self.__salary = salary
        self.__credit_score = credit_score
        self.__student_age = student_age

    def check_eligibility(self):
        if (
            self.__salary >= 25000
            and self.__credit_score >= 650
            and self.__student_age <= 25
        ):
            print("education loan is approved")
        else:
            print("education loan is rejected")


HL = HomeLoan("nagaraj", 60000, 750, False)
EL = EducationLoan("rahulla", 30000, 630, 22)
HL.check_eligibility()
EL.check_eligibility()
# GETTER USED WHEN WE CALL IT FROM OUTSIDE, HERE INSISDE CHILD CLAASS PRIVATE ATTRIBUTE CAN BE CALLED


""" Q28 — Cab Booking & Fare System

Write a Python program using Abstraction + Encapsulation + Multiple Child Classes + Different Fare Logic.

1. Abstract class Cab

Create:

class Cab(ABC):

Abstract method:

calculate_fare(self, distance)
2. Child class MiniCab

Private attributes:

__driver_name
__base_fare

Getters:

get_driver_name()
get_base_fare()

Fare rule:

Fare = base_fare + (distance × 15)

But:

If distance <= 0 → "Invalid distance"
If distance > 20 km → add ₹100 extra charge
3. Child class PremiumCab

Private attributes:

__driver_name
__base_fare
__rating

Getters:

get_driver_name()
get_rating()

Fare rule:

Fare = base_fare + (distance × 25)

But:

If distance <= 0 → "Invalid distance"
If rating >= 4.5 → give ₹50 discount
Otherwise → no discount"""

from abc import ABC, abstractmethod


class Cab(ABC):
    @abstractmethod
    def calculate_fare(self, distance):
        pass


class MiniCab(Cab):
    def __init__(self, driver_name, base_fare):
        self.__driver_name = driver_name
        self.__base_fare = base_fare

    def get_driver_name(self):
        return self.__driver_name

    def get_base_fare(self):
        return self.__base_fare

    def calculate_fare(self, distance):
        print("Driver:", self.__driver_name)

        if distance <= 0:
            print("Invalid distance")

        else:
            total_fare = self.__base_fare + (distance * 15)

            if distance > 20:
                total_fare = total_fare + 100
                print("₹100 extra charge")

            print("Mini Cab Fare:", total_fare)


class PremiumCab(Cab):
    def __init__(self, driver_name, base_fare, rating):
        self.__driver_name = driver_name
        self.__base_fare = base_fare
        self.__rating = rating

    def get_driver_name(self):
        return self.__driver_name

    def get_base_fare(self):
        return self.__base_fare

    def get_rating(self):
        return self.__rating

    def calculate_fare(self, distance):
        print("Driver:", self.__driver_name)

        if distance <= 0:
            print("Invalid distance")

        else:
            total_fare = self.__base_fare + (distance * 25)

            if self.__rating >= 4.5:
                total_fare = total_fare - 50
                print("₹50 discount applied")

            print("Premium Cab Fare:", total_fare)


mini_cab = MiniCab("Nagaraj", 100)
premium_cab = PremiumCab("Rahulla", 200, 4.7)

mini_cab.calculate_fare(25)

print()

premium_cab.calculate_fare(10)
