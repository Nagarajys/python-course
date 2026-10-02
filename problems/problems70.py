# Problem 4/30 — Hierarchical Inheritance


from itertools import pairwise


class Employe:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print("Name", self.name)


class Manager(Employe):
    def __init__(self, name, team_size):
        super().__init__(name)
        self.team_size = team_size

    def show_manager(self):
        self.show_name()
        print("Team_size:", self.team_size)


class Designer(Employe):
    def __init__(self, name, tool):
        super().__init__(name)
        self.tool = tool

    def show_designer(self):
        self.show_name()
        print("Tool:", self.tool)


manager = Manager("Nagaraj", 8)
designer = Designer("karthik", "figma")
manager.show_manager()
designer.show_designer()


# 5/30 — Hybrid Inheritance
class Person:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print("Name:", self.name)


class Student(Person):
    def __init__(self, name, course):
        Person.__init__(self, name)
        self.course = course

    def show_student(self):
        print("Course:", self.course)


class Employee(Person):
    def __init__(self, name, company):
        Person.__init__(self, name)
        self.company = company

    def show_employee(self):
        print("Company:", self.company)


class Intern(Student, Employee):
    def __init__(self, name, course, company, duration):
        Student.__init__(self, name, course)
        Employee.__init__(self, name, company)
        self.duration = duration

    def show_intern(self):
        self.show_name()
        self.show_student()
        self.show_employee()
        print("Duration:", self.duration, "months")


intern = Intern("Sutej", "CSE AIML", "Microsoft", 6)

intern.show_intern()


# Problem 6/30 — Polymorphism: Method Overriding
class payment:
    def pay(self):
        print("processing payment")


class UPIpayment(payment):
    def pay(self):
        print("paid 500 using UPI")


class cardpayment(payment):
    def pay(self):
        print("paid 1000 using CARD")


upi = UPIpayment()
card = cardpayment()
upi.pay()
card.pay()


# Problem 7/30 — Polymorphism
class DeliveryPartner:
    def __init__(self, distance):
        self.distance = distance

    def calculate_charge(self):
        pass


class BikeDelivery(DeliveryPartner):
    def calculate_charge(self):
        print("bike delivery charge", self.distance * 10)


class CarDelivery(DeliveryPartner):
    def calculate_charge(self):
        print("car delivery charge", self.distance * 20)


class premiumDelivery(DeliveryPartner):
    def calculate_charge(self):
        print("premium delivery charge", self.distance * 35)


BD = BikeDelivery(5)
CD = CarDelivery(5)
PD = premiumDelivery(5)
BD.calculate_charge()
CD.calculate_charge()
PD.calculate_charge()


# Problem 8/30 — Polymorphism
class Notification:
    def send(self, message):
        pass


class EmailNotification(Notification):
    def send(self, message):
        print("Email:", message)


class SMSNotification(Notification):
    def send(self, message):
        print("SMS:", message)


class PushNotification(Notification):
    def send(self, message):
        print("Push Notification:", message)


email = EmailNotification()
sms = SMSNotification()
push = PushNotification()

email.send("Your order has been shipped")
sms.send("Your order has been shipped")
push.send("Your order has been shipped")


# Problem 9/30 — Polymorphism
class Report:
    def genrate(self):
        pass


class salesReport(Report):
    def genrate(self):
        print("genrating sales Report")


class attendenceReport(Report):
    def genrate(self):
        print("genrating attendence Report")


class FinanceReport(Report):
    def genrate(self):
        print("genrating Finance report")


sales = salesReport()
attendance = attendenceReport()
finance = FinanceReport()
sales.genrate()
attendance.genrate()
finance.genrate()


# Problem 10/30 — Polymorphism
class shipping:
    def calculate_cost(self, weight):
        pass


class standardShipping(shipping):
    def calculate_cost(self, weight):
        print("standard shipping:", weight * 40)


class ExpressShipping(shipping):
    def calculate_cost(self, weight):
        print("express shipping:", weight * 80)


class InternationalShipping(shipping):
    def calculate_cost(self, weight):
        print("International shipping:", weight * 200)


standard = standardShipping()
express = ExpressShipping()
international = InternationalShipping()
standard.calculate_cost(3)
express.calculate_cost(3)
international.calculate_cost(3)


# Problem 11/30 — Polymorphism
class process:
    def process(self):
        pass


class imageprocesser(process):
    def process(self):
        print("processing image")


class textprocesser(process):
    def process(self):
        print("processing text")


class audioprocesser(process):
    def process(self):
        print("audio processer")


objects = [imageprocesser(), textprocesser(), audioprocesser()]
for obj in objects:
    obj.process()


# Problem 12/30 — Polymorphism
class Employes:
    def calculate_salary(self):
        pass


class FullTimeEmployee(Employes):
    def __init__(self, salary):
        self.salary = salary

    def calculate_salary(self):
        print("full time employee:", self.salary)


class PartTime(Employes):
    def __init__(self, salary, hours):
        self.salary = salary
        self.hours = hours

    def calculate_salary(self):
        print("part time:", self.salary * self.hours)


class free_lancer(Employes):
    def __init__(self, salary, projects):
        self.salary = salary
        self.projects = projects

    def calculate_salary(self):
        print("free lancer salary:", self.salary * self.projects)


employe1 = FullTimeEmployee(50000)
employe2 = PartTime(500, 80)
employe3 = free_lancer(1500, 8)
employe1.calculate_salary()
employe2.calculate_salary()
employe3.calculate_salary()


# Problem 13/30 — Polymorphism: Method with Different Input Data:
# vehical rental system


class Vehicle:
    def __init__(self, vehicle_number):
        self.vehicle_number = vehicle_number

    def calculate_rent(self, days):
        pass


class Bike(Vehicle):
    def calculate_rent(self, days):
        print("Vehicle:", self.vehicle_number)
        print("Bike rent:", days * 300)


class Car(Vehicle):
    def calculate_rent(self, days):
        print("Vehicle:", self.vehicle_number)
        print("Car rent:", days * 800)


class LuxuryCar(Vehicle):
    def calculate_rent(self, days):
        print("Vehicle:", self.vehicle_number)
        print("Luxury car rent:", days * 2000)


bike = Bike("KA01AB1234")
car = Car("KA02CD5678")
luxury_car = LuxuryCar("KA03EF9012")

bike.calculate_rent(30)
car.calculate_rent(60)
luxury_car.calculate_rent(10)
