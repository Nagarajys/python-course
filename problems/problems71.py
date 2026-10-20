# Problem 14/30 — Advanced Polymorphism: Payment Gateway System
class payment:
    def __init__(self, ID):
        self.ID = ID

    def process_payment(self, amount):
        pass


class UPI(payment):
    def process_payment(self, amount):
        processing_fee = amount * (2 / 100)
        final_amount = amount + processing_fee
        print("PAYMENT ID:", self.ID)
        print("PROCESSING FEE = ", processing_fee)
        print("FINAL AMOUNT = ", final_amount)


class Card(payment):
    def process_payment(self, amount):
        processing_fee = amount * (3 / 100)
        final_amount = amount + processing_fee
        print("PAYMENT ID:", self.ID)
        print("PROCESSING FEE = ", processing_fee)
        print("FINAL AMOUNT = ", final_amount)


class Wallet(payment):
    def process_payment(self, amount):
        processing_fee = amount * (1 / 100)
        if amount >= 2000:
            discount = 50
        else:
            discount = 0
        final_amount = amount + processing_fee - discount
        print("PAYMENT ID:", self.ID)
        print("DISCOUNT:", discount)
        print("PROCESSING FEE = ", processing_fee)
        print("FINAL AMOUNT = ", final_amount)


big_payments = [UPI(" UPI9876 "), Card("CARD4521"), Wallet("WALLET789 ")]
money = [1500, 3000, 2500]
for big_pay, money_value in zip(big_payments, money):
    big_pay.process_payment(money_value)


# Problem 15 — Ride Fare System:
class Ride:
    def __init__(self, ride_id, customer_name):
        self.ride_id = ride_id
        self.customer_name = customer_name

    def clacualate_fare(self, distance):
        pass


class BikeRide(Ride):
    def calculate_fare(self, distance):
        base_fare = 50
        per_km = 10
        total_fare = base_fare + (distance * per_km)
        print("RIDE ID=", self.ride_id)
        print("CUSTOMER NAME=", self.customer_name)
        print("TOTAL FARE= ", total_fare)


class AutoRide(Ride):
    def calculate_fare(self, distance):
        base_fare = 50
        per_km = 15
        total_fare = base_fare + (distance * per_km)
        print("RIDE ID=", self.ride_id)
        print("CUSTOMER NAME=", self.customer_name)
        print("TOTAL FARE= ", total_fare)


class CabRide(Ride):
    def calculate_fare(self, distance):
        base_fare = 80
        per_km = 20
        total_fare = base_fare + (distance * per_km)
        print("RIDE ID=", self.ride_id)
        print("CUSTOMER NAME=", self.customer_name)
        print("TOTAL FARE= ", total_fare)


class PremiumCab(Ride):
    def calculate_fare(self, distance):
        base_fare = 50
        per_km = 10
        total_fare = base_fare + (distance * per_km)
        print("RIDE ID=", self.ride_id)
        print("CUSTOMER NAME=", self.customer_name)
        print("TOTAL FARE= ", total_fare)


Journey_ride = [
    BikeRide("R101", "nagaraj"),
    AutoRide("R102", "karthik"),
    CabRide("R103", "rahullla"),
    PremiumCab("R104", "arjuna"),
]
distances = (10, 8, 12, 5)
for journey, distance in zip(Journey_ride, distances):
    journey.calculate_fare(distance)
