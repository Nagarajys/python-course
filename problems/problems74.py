"""Problem 21/30 — Advanced Interview Question
Smart Hospital Monitoring System

Imagine you are developing the backend of a hospital monitoring system.

The hospital has different types of monitoring devices such as HeartMonitor, TemperatureMonitor, and OxygenMonitor.

The system should:

Store basic device information.
Each device should have its own way of generating a monitoring report.
The device's internal monitoring value should not be directly accessible from outside the class.
The hospital should be able to manage multiple monitoring devices together and generate reports from all of them.
Design the system using all four pillars of OOP.
Demonstrate polymorphism by processing different device objects through a common interface.


*** Interview expectation
**Interviewer will expect you to decide:

Which classes should exist?
Where inheritance makes sense?
What should be private?
Which method should be abstract?
How multiple objects should be processed polymorphically?
How one class can contain/manage other objects."""

from abc import ABC, abstractmethod


############### patient side############
class Patient(ABC):  # base class
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_patient_type(self) -> str:
        pass


class HeartPatient(Patient):  # childs
    def get_patient_type(self):
        return "Heart Patient"


class MalariaPatient(Patient):
    def get_patient_type(self):
        return "Malaria Patient"


class LungsCancerPatient(Patient):
    def get_patient_type(self):
        return "LungCancerPatient"


# -------------monitor side--------------#
class Monitor(ABC):  # base classs
    def __init__(self, value):
        self.__value = value

    def get_value(self):
        return self.__value  # controlledd acess to get private value

    @abstractmethod
    def process(self):
        pass


class HeartMonitor(Monitor):  # child class
    def process(self):
        print("heart monitor processing")
        print("heart reading:", self.get_value())  # calling the  controlled access


class TemperatureMonitor(Monitor):  # child class
    def process(self):
        print("temperature monitor processing")
        print(
            "temperature reading:", self.get_value()
        )  # calling the  controlled access


class OxygenMonitor(Monitor):  # child class
    def process(self):
        print("oxygen monitor processing")
        print("oxygen reading:", self.get_value())  # calling the  controlled access


# --------------hospital-------------------#
class Hospital:
    def __init__(self, patient, monitor):
        self.patient = patient
        self.monitor = monitor

    def generate_report(self):
        print("\nPATIENT", self.patient.name)
        print("TYPE", self.patient.get_patient_type())
        self.monitor.process()


# --------------objects-------------#
heart_patient = HeartPatient("rahulla")
malaria_patient = MalariaPatient("arun")
lung_patient = LungsCancerPatient("kiran")


heart_monitor = HeartMonitor(80)
temperature_monitor = TemperatureMonitor(45)
oxygen_monitor = OxygenMonitor(95)

# --------------patient ++ corresponding monitor--------------------#
hospital_records = [
    Hospital(heart_patient, heart_monitor),
    Hospital(malaria_patient, temperature_monitor),
    Hospital(lung_patient, oxygen_monitor),
]

# process all records
for record in hospital_records:
    record.generate_report()


"""             Patient
                ↑
       ┌────────┼────────┐
       ↓        ↓        ↓
 HeartPatient MalariaPatient LungCancerPatient


             Monitor
                ↑
       ┌────────┼──────────┐
       ↓        ↓          ↓
HeartMonitor TemperatureMonitor OxygenMonitor


              Hospital
             /        \
          HAS-A       HAS-A
            ↓           ↓
         Patient     Monitor"""


"""Q22/30 — Advanced Interview Question
Movie Streaming System

You're developing the backend of a movie-streaming platform.

The platform has different types of content such as Movie, Series, and Documentary.

Each content type should have its own way of calculating the watching charge.

A user can create a personal watchlist and add multiple content objects to it. The watchlist should be able to display all added content and calculate their charges.

The system should also protect the user's watchlist data from direct external modification"""


from abc import ABC, abstractmethod


class User(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_user(self) -> str:  # -> str doesn't convert anything.
        pass  # It is just a type annotation telling us:


class Youngers(User):
    def get_user(self):
        return "Youngers"


class Adults(User):
    def get_user(self):
        return "Adults"


class SeniorCitizen(User):
    def get_user(self):
        return "Senior Citizens"


class content(ABC):
    def __init__(self, content, charge, user):
        self.__content = content
        self.__charge = charge
        self.user = user

    def get_content(self):
        return self.__content

    def get_charge(self):
        return self.__charge

    def get_user(self):
        return self.user.get_user()

    def get_user_name(self):
        return self.user.name

    @abstractmethod
    def show_content(self):  # method
        pass


class Movie(content):
    def show_content(self):
        print("\nMOVIE PROCESSING")
        print("CONTENT NAME:", self.get_content())
        print("USER NAME:", self.get_user_name())
        print("USER TYPE:", self.get_user())

        charge = self.get_charge()
        if self.get_user() == "Youngers":
            discount = 25
            charge = charge - discount
        elif self.get_user() == "Adults":
            discount = 12
            charge = charge - discount
        elif self.get_user() == "Senior Citizens":
            discount = charge
            charge = charge - discount
        print("WATCHING CHARGE:", charge)


class Series(content):
    def show_content(self):
        print("\nSERIES PROCESSING")
        print("CONTENT NAME:", self.get_content())
        print("USER NAME:", self.get_user_name())
        print("USER TYPE:", self.get_user())

        charge = self.get_charge()
        if self.get_user() == "Youngers":
            discount = 25
            charge = charge - discount
        elif self.get_user() == "Adults":
            discount = 12
            charge = charge - discount
        elif self.get_user() == "Senior Citizens":
            discount = charge
            charge = charge - discount
        print("WATCHING CHARGE:", charge)


class Documentary(content):
    def show_content(self):
        print("\nSERIES PROCESSING")
        print("CONTENT NAME:", self.get_content())
        print("USER NAME:", self.get_user_name())
        print("USER TYPE:", self.get_user())
        charge = self.get_charge()
        if self.get_user() == "Youngers":
            discount = 25
            charge = charge - discount
        elif self.get_user() == "Adults":
            discount = 12
            charge = charge - discount
        elif self.get_user() == "Senior Citizens":
            discount = charge
            charge = charge - discount
        print("WATCHING CHARGE:", charge)


user1 = Youngers("nagaraj")
user2 = Adults("subramanya")
user3 = SeniorCitizen("rangaswamy")

movies = [
    Movie("kgf", 200, user1),
    Movie("toxic", 150, user2),
    Movie("Devil", 500, user3),
]
seri = [
    Series("anime", 200, user1),
    Series("tokyo revengers", 150, user2),
    Series("horror", 500, user3),
]
documentaries = [
    Documentary("rich dad", 200, user1),
    Documentary("Poor dad", 150, user2),
    Documentary("power law", 500, user3),
]

for movie in movies:
    movie.show_content()
for ser in seri:
    ser.show_content()
for documents in documentaries:
    documents.show_content()


"""Q23 — Food Subscription System

Design a Food Subscription System using Python OOP.

A company offers different subscription plans:

Basic Plan
Premium Plan
Family Plan

Each plan should have its own way of calculating the monthly bill.

A customer can subscribe to a plan and can also add extra meals during the month. The system should calculate the final amount based on the selected plan and extra meals.

Requirements
Store customer details.
Different subscription plans must behave differently when calculating the bill.
Subscription details should not be directly accessible/modifiable from outside.
The system should allow a customer to add extra meals.
Process multiple customers/subscriptions together using a collection + loop.
Display:
Customer name
Plan type
Extra meals
Final bill
Use all four OOP pillars.
Use polymorphism when processing different subscription plans.
Don't use the same structure as the previous Movie/Streaming question."""


class Company:
    def __init__(self, customer_name, basic_plan, premium_plan, family_plan):
        self.customer_name = customer_name
        self.__basic_plan = basic_plan
        self.__premium_plan = premium_plan
        self.__family_plan = family_plan

    def get_basic_plan(self):
        return self.__basic_plan

    def get_premium_plan(self):
        return self.__premium_plan

    def get_family_plan(self):
        return self.__family_plan

    def accessibility(self):
        pass


class Subscription(Company):
    def __init__(
        self, customer_name, basic_plan, premium_plan, family_plan, selected_plan
    ):
        super().__init__(customer_name, basic_plan, premium_plan, family_plan)
        self.__status = False
        self.selected_plan = selected_plan

    def accessibility(self):
        self.__status = True
        print("customer_name:", self.customer_name)
        print("subscription status:", "SUBSCRIBED SUCESSFULLY")

    def Show_status(self):
        if self.selected_plan == "Basic_plan":
            print("YOU CHOOSEN BASIC PLAN")
        elif self.selected_plan == "Premium_plan":
            print("YOU CHOOSEN PREMIUM PLAN")
        elif self.selected_plan == "Family_plan":
            print("YOU CHOOSEN FAMILY PLAN")


class PlanType(ABC):
    def __init__(self, bill, extra_meals):
        self.bill = bill
        self.extra_meals = extra_meals

    @abstractmethod
    def payment_process(self):
        pass


class BasicPlan(PlanType):
    def payment_process(self):
        print("Initialbill:", self.bill)
        extra_meal_bill = 50
        final_bill = self.bill + (extra_meal_bill * self.extra_meals)
        print(" BASIC PLAN FINAL BILL", final_bill)


class PremiumPlan(PlanType):
    def payment_process(self):
        print("Initialbill:", self.bill)
        extra_meal_bill = 100
        final_bill = self.bill + (extra_meal_bill * self.extra_meals)
        print(" PREMIUM PLAN FINAL BILL", final_bill)


class FamilyPlan(PlanType):
    def payment_process(self):
        print("Initialbill:", self.bill)
        extra_meal_bill = 75
        final_bill = self.bill + (extra_meal_bill * self.extra_meals)
        print(" FAMILY PLAN FINAL BILL", final_bill)


customer1 = Subscription("nagaraj", 500, 1000, 1500, "Basic_plan")
customer2 = Subscription("subramanya", 500, 1000, 1500, "Premium_plan")
customer3 = Subscription("vani", 500, 1000, 1500, "Family_plan")
customer1.accessibility()
customer2.accessibility()
customer3.accessibility()
customer1.Show_status()
customer2.Show_status()
customer3.Show_status()

basic = BasicPlan(500, 6)
premium = PremiumPlan(1000, 12)
family = FamilyPlan(1500, 20)

plans = [basic, premium, family]
for plan in plans:
    plan.payment_process()
