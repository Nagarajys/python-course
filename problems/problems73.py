# problem 19:
# e commerce paymentn system:
"""“Design an E-Commerce Payment System using Python OOP.

The system should manage products and orders. An order should maintain its status securely.

The system should support different payment methods such as UPI, Card, and Wallet, where each payment method has its own way of calculating the transaction charge.

Design the system using the four pillars of OOP and demonstrate polymorphism while processing different payment methods.”
"""

from abc import ABC, abstractmethod


class Product:
    def __init__(self, customer_name, product_id):
        self.customer_name = customer_name
        self.product_id = product_id


class Order(Product):
    def __init__(self, customer_name, product_id):
        super().__init__(customer_name, product_id)
        self.__status = False  # initially order status is pending

    def order_details(self):
        self.__status = True  # here order will be conformed
        print("customer name:", self.customer_name)
        print("product id:", self.product_id)

    def show_status(self):
        if self.__status == True:
            print("ORDER STATUS:", "YOUR ORDER HAS BEEN CONFORMED")
        else:
            print("ORDER STATUS:", "ORDER CONFORMATION IS PENDING")


class Payment(ABC):
    @abstractmethod
    def payment_process(self, amount, percent):
        pass


class UPI(Payment):
    def payment_process(self, amount, percent):
        charge = (
            amount * percent / 100
        )  # to calculate transaction charge while paying through upi
        final_amount = amount + charge
        print("amount:", amount)
        print("transaction charge:", charge)
        print("final amount:", final_amount)


class Card(Payment):
    def payment_process(self, amount, percent):
        charge = (
            amount * percent / 100
        )  # to calculate transaction charge while paying through card
        final_amount = amount + charge
        print("amount:", amount)
        print("transaction charge:", charge)
        print("final amount:", final_amount)


class Wallet(Payment):
    def payment_process(self, amount, percent):
        charge = (
            amount * percent / 100
        )  # to calculate transaction charge while paying through Wallet
        final_amount = amount + charge
        print("amount:", amount)
        print("transaction charge:", charge)
        print("final amount:", final_amount)


product_information = Order("sutej", "ka56077")
product_information.order_details()
product_information.show_status()

methods = [UPI(), Card(), Wallet()]
amts = [68, 97, 144]
deliver_charges = [2, 6, 11]
for method, amt, charge in zip(methods, amts, deliver_charges):
    method.payment_process(amt, charge)


"""Problem 20/30

“Design a Hospital Appointment System using Python OOP.

The system should manage doctors and patients. A patient should be able to book an appointment with a doctor, and the appointment should maintain its status.

The system should support different types of doctors, where each doctor has a different consultation fee.

Design the system using the four pillars of OOP and demonstrate polymorphism when calculating the consultation fees.”"""


from abc import ABC, abstractmethod


class Hospital:
    def __init__(self, patient_name, patient_location, mobile_number):
        self.patient_name = patient_name
        self.patient_location = patient_location
        self.mobile_number = mobile_number


class Doctor(Hospital):
    def __init__(self, patient_name, patient_location, mobile_number):
        super().__init__(patient_name, patient_location, mobile_number)
        self.__appointment = False  # initiallt not approved

    def patient_details(self):
        self.__appointment = True
        print("PATIENT NAME:", self.patient_name)
        print("PATIENT LLOCATION :", self.patient_location)
        print("MOBILE NUMBER:", self.mobile_number)

    def show_status(self):
        if self.__appointment == True:
            print("Appointment status:", self.patient_name, "has been appointed")
        else:
            print("Appointment status:", "NOT APPROVED")


class Doctors(ABC):
    @abstractmethod
    def consultation_fee(self):
        pass


class Genral_doctor(Doctors):
    def consultation_fee(self):
        amount = 1500
        print("Consultation fees for Genral doctor:", amount)


class Specialist(Doctors):
    def consultation_fee(self):
        amount = 5000
        print("Consultation fees for Specialist doctor:", amount)


class Surgen(Doctors):
    def consultation_fee(self):
        amount = 10000
        print("Consultation fees for Surgen doctor:", amount)


registered_patients = Doctor("rahul", "shivamogga", 6361273988)
registered_patients.patient_details()
registered_patients.show_status()
specialists = [Genral_doctor(), Specialist(), Surgen()]
for specialist in specialists:
    specialist.consultation_fee()
