class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


student1 = Student("Nagaraj", 18)
student2 = Student("Rahul", 19)

student1.display()
student2.display()


"""Student       → Class
Student(...)  → Create object
__init__()    → Automatically runs
self          → Current object
name          → Received value
self.name     → Current object's name
self.name=name → Store name inside object"""


"""Student → class
Student("Nagaraj", 18) → creates the object
student1 → that object-na reference/name
self → currently created object
self.name → that object's name data
self.age → that object's age data"""


## THE 4 PILLARS OF OOPl:
# 1. ENCAPSULATION:
class bankaccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance = self.__balance + amount
        else:
            print("invalid amount")

    def check_balance(self):
        return self.__balance


account = bankaccount(50000)
account.deposit(10000)
print(account.check_balance())


class bankaccounts:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount


account = bankaccounts(50000)
print(account.get_balance())
account.set_balance(8000000)
print(account.get_balance())  # must call function here
