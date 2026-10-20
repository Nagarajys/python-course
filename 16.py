# Topic - Solids Principles in Python:::
# 1 . single responsibnility principle:
# 1. Calculate percentage
class CalculateResult:
    def calculate_percentage(self, marks, total_marks):
        return marks * 100 / total_marks


# 2. Display result
class ShowResult:
    def display_result(self, name, percentage):
        print(f"Student: {name}")
        print(f"Percentage: {percentage}%")


# 3. Store result
class StoreResult:
    def save_result(self, name, percentage):
        with open("result.txt", "w") as file:
            file.write(f"{name}: {percentage}%")


calculator = CalculateResult()

percentage = calculator.calculate_percentage(450, 500)

print(percentage)


# 2. OCP - OPEN OR CLOSED PRINCIPLE:
from abc import ABC, abstractmethod


class Notification(ABC):
    @abstractmethod
    def send(self, method, message):
        pass


class Email(Notification):
    def send(self, method, message):
        print(f"sending notification through,{method}:{message}")


class SMS(Notification):
    def send(self, method, message):
        print(f"sending notification through,{method}:{message}")


class Whatsapp(Notification):
    def send(self, method, message):
        print(f"sending notification through,{method}:{message}")


class Facebook(Notification):
    def send(self, method, message):
        print(f"sending notification through,{method}:{message}")


class Instagram(Notification):
    def send(self, method, message):
        print(f"sending notification through,{method}:{message}")


class Snapchat(Notification):
    def send(self, method, message):
        print(f"sending notification through,{method}:{message}")


email = Email()
sms = SMS()
whatsapp = Whatsapp()
face = Facebook()
insta = Instagram()
snapchat = Snapchat()
email.send("EMAIL", "SUTEJ YOU ARE SELECTED FOR MICROSFT WITH A STIPEND OF 25LPA")
sms.send("SMS", "SATISH YOU ARE SELECTED FOR GOOOGLE WITH A STIPEND OF 28LPA ")
whatsapp.send(
    "WHATSAPP", "NISHANTH YOU ARE SELECTED FOR GOOOGLE WITH A STIPEND OF 28LPA "
)
face.send("FACE", "SATISH YOU ARE SELECTED FOR GOOOGLE WITH A STIPEND OF 28LPA ")
insta.send("INSTAGRAM", "NAGARAJ YOU ARE SELECTED FOR INFOSYS WITH A STIPEND OF 3LPA ")
snapchat.send("SMS", "SATISH YOU ARE SELECTED FOR GOOOGLE WITH A STIPEND OF 28LPA ")


# 1.LSP
class UPIPayment:
    def pay(self, amount):
        print(f"UPI payment of ₹{amount} successful")


class CardPayment:
    def pay(self, amount):
        print(f"Card payment of ₹{amount} successful")


def process_payment(payment):
    payment.pay(1000)


upi = UPIPayment()
card = CardPayment()

process_payment(upi)
process_payment(card)

# ISP:
# a class should have the methods which needed to it dont force other extra methods:
from abc import ABC, abstractmethod


class Teaching(ABC):
    def teach(self):
        pass


class Coding(ABC):
    def write_code(self):
        pass


class Cleaning(ABC):
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
