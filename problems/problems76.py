# OOP CHALLENGES:
# 1.BANKING SYSTEM SIMULATION:
# design a system to stimulate a bank"s operation,
# Here user can able to #1.create account , 2. deposit  , 3. withdarw money , 4. check balamnce
# ACCOUNT -> SAVINGS ACCOUNT -> CURRENT ACCOUNT
# each account should have unique behavior - 1. intrest calculation or overdraft limits
# finally use encapsulation  , abstractionn  , inheritance ,  polymorphismmm
# bank should contain bank name , city name  ,  user id(account number) ,  use name

from abc import ABC


# Parent class
class Account(ABC):
    def __init__(self, user_id, user_name):
        self.user_id = user_id
        self._user_name = user_name
        self._balance = 0

    def check_balance(self):
        print(f"Current balance: ₹{self._balance}")

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited successfully: ₹{amount}")
            self.check_balance()
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
        elif amount <= self._balance:
            self._balance -= amount
            print(f"Withdrawn successfully: ₹{amount}")
            self.check_balance()
        else:
            print("Insufficient balance.")


# Child class 1
class SavingsAccount(Account):
    def calculate_interest(self):
        interest_rate = 0.08
        interest = self._balance * interest_rate
        print(f"Interest earned at 8%: ₹{interest:.2f}")


# Child class 2
class CurrentAccount(Account):
    def withdraw(self, amount):
        overdraft_limit = 2000

        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
        elif amount <= self._balance + overdraft_limit:
            self._balance -= amount
            print(f"Withdrawn successfully: ₹{amount}")
            self.check_balance()
        else:
            print("Overdraft limit exceeded.")


# Bank class
class Bank:
    def __init__(self, bank_name, city):
        self.bank_name = bank_name
        self.city = city
        self.__accounts = {}

    def create_account(self, user_id, holder_name, account_type):
        if user_id in self.__accounts:
            print("Account ID already exists.")
            return None

        if account_type == SavingsAccount:
            new_account = SavingsAccount(user_id, holder_name)
        elif account_type == CurrentAccount:
            new_account = CurrentAccount(user_id, holder_name)
        else:
            print("Invalid account type.")
            return None

        self.__accounts[user_id] = new_account
        print(f"{account_type.__name__} created for {holder_name}.")
        return new_account

    def get_account(self, user_id):
        account = self.__accounts.get(user_id)

        if account is None:
            print("Account not found.")
            return None

        print(f"Account ID: {account.user_id}")
        print(f"Holder name: {account._user_name}")
        return account


# Create bank
nbk = Bank("Nagaraj Bank of Karnataka", "Shivamogga")

# Create accounts
acc1 = nbk.create_account(1, "RAJA", SavingsAccount)
acc2 = nbk.create_account(2, "Subramanya", CurrentAccount)

# Savings account operations
if isinstance(acc1, SavingsAccount):
    acc1.deposit(1000)
    acc1.calculate_interest()

# Current account operations
if isinstance(acc2, CurrentAccount):
    acc2.deposit(500)
    acc2.withdraw(2000)
    acc2.check_balance()


# 2. STUDENT REPORT CARD GENRATOR
# sytem should collects student data , subj wise marks , to genrate a reportcard

# here include grade calculation , avg score , passor fail
# encapsualtion for mark storage and abstraction for result genrationnnn


"""class student - base class 
*student name
*roll number

class details - child class 
def show stastus
* all subject should be passed to get report card

class exams - abstract classs
method evalvation
class physics of sub - grade calculation1 a ,b ,c and fail pass
class chem
ckass bio
clas math
class kan 
claass eng 
check grade and marks , at last calcualte avg marks
"""
from abc import ABC, abstractmethod


class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number

    def eligibility_status(self):
        pass


class details(Student):
    def __init__(self, name, roll_number, entered_roll_number):
        super().__init__(name, roll_number)
        self.status = False
        self.entered_roll_number = entered_roll_number

    def eligibility_status(self):
        if self.roll_number == self.entered_roll_number:
            self.status = True
            print("You are eligible for exam")
        else:
            self.status = False
            print("Roll number mismatch")


class Exams(ABC):
    def __init__(self, theory_marks, practical_marks):
        self.__theory_marks = theory_marks
        self.__practical_marks = practical_marks

    def get_theory_marks(self):
        return self.__theory_marks

    def get_practical_marks(self):
        return self.__practical_marks

    @abstractmethod
    def evalvation(self):
        pass


class Physics(Exams):
    def evalvation(self):
        theory = self.get_theory_marks()
        practical = self.get_practical_marks()
        total = theory + practical

        if theory >= 65 and practical >= 18:
            print("GRADE A")
        elif theory >= 55 and practical >= 15:
            print("GRADE B")
        elif theory >= 35 and practical >= 12:
            print("GRADE C")
        else:
            print("RESULT = FAIL. TRY TO WRITE EXAM AGAIN")

        print("MARKS:", total)
        return total


class Chemistry(Exams):
    def evalvation(self):
        theory = self.get_theory_marks()
        practical = self.get_practical_marks()
        total = theory + practical

        if theory >= 65 and practical >= 18:
            print("GRADE A")
        elif theory >= 55 and practical >= 15:
            print("GRADE B")
        elif theory >= 35 and practical >= 12:
            print("GRADE C")
        else:
            print("RESULT = FAIL. TRY TO WRITE EXAM AGAIN")

        print("MARKS:", total)
        return total


class Biology(Exams):
    def evalvation(self):
        theory = self.get_theory_marks()
        practical = self.get_practical_marks()
        total = theory + practical

        if theory >= 65 and practical >= 18:
            print("GRADE A")
        elif theory >= 55 and practical >= 15:
            print("GRADE B")
        elif theory >= 35 and practical >= 12:
            print("GRADE C")
        else:
            print("RESULT = FAIL. TRY TO WRITE EXAM AGAIN")

        print("MARKS:", total)
        return total


class Maths(Exams):
    def evalvation(self):
        theory = self.get_theory_marks()
        practical = self.get_practical_marks()
        total = theory + practical

        if theory >= 75 and practical >= 18:
            print("GRADE A")
        elif theory >= 55 and practical >= 15:
            print("GRADE B")
        elif theory >= 35 and practical >= 12:
            print("GRADE C")
        else:
            print("RESULT = FAIL. TRY TO WRITE EXAM AGAIN")

        print("MARKS:", total)
        return total


class English(Exams):
    def evalvation(self):
        theory = self.get_theory_marks()
        practical = self.get_practical_marks()
        total = theory + practical

        if theory >= 75 and practical >= 18:
            print("GRADE A")
        elif theory >= 55 and practical >= 15:
            print("GRADE B")
        elif theory >= 35 and practical >= 12:
            print("GRADE C")
        else:
            print("RESULT = FAIL. TRY TO WRITE EXAM AGAIN")

        print("MARKS:", total)
        return total


class Kannada(Exams):
    def evalvation(self):
        theory = self.get_theory_marks()
        practical = self.get_practical_marks()
        total = theory + practical

        if theory >= 75 and practical >= 18:
            print("GRADE A")
        elif theory >= 55 and practical >= 15:
            print("GRADE B")
        elif theory >= 35 and practical >= 12:
            print("GRADE C")
        else:
            print("RESULT = FAIL. TRY TO WRITE EXAM AGAIN")

        print("MARKS:", total)
        return total


name = input("Enter student name: ")
roll_number = input("Enter registered roll number: ")
entered_roll_number = input("Enter roll number for verification: ")

student = details(name, roll_number, entered_roll_number)
student.eligibility_status()

if student.status:
    physics = Physics(
        int(input("physics theory marks:")), int(input("physics practical marks: "))
    )
    chemistry = Chemistry(
        int(input("chemistry theory marks: ")), int(input("chemistry practical marks:"))
    )
    biology = Biology(
        int(input("Biology theory marks: ")), int(input("Biology practical marks: "))
    )

    maths = Maths(
        int(input("Maths theory marks: ")), int(input("Maths practical marks: "))
    )

    english = English(
        int(input("English theory marks: ")), int(input("English practical marks: "))
    )

    kannada = Kannada(
        int(input("Kannada theory marks: ")), int(input("Kannada practical marks: "))
    )
    # Generate report card
    print("\n========== REPORT CARD ==========")
    print("Student Name:", student.name)
    print("Roll Number:", student.roll_number)

    # Evaluate each subject
    print("\n--- PHYSICS ---")
    total1 = physics.evalvation()

    print("\n--- CHEMISTRY ---")
    total2 = chemistry.evalvation()

    print("\n--- BIOLOGY ---")
    total3 = biology.evalvation()

    print("\n--- MATHS ---")
    total4 = maths.evalvation()

    print("\n--- ENGLISH ---")
    total5 = english.evalvation()

    print("\n--- KANNADA ---")
    total6 = kannada.evalvation()

    # Calculate grand total
    grand_total = total1 + total2 + total3 + total4 + total5 + total6

    # Calculate average
    average = grand_total / 6

    print("\n========== FINAL RESULT ==========")
    print("Grand Total:", grand_total, "/ 780")
    print("Average Marks:", round(average, 2), "/ 130")

    # Overall pass/fail check
    if (
        physics.get_theory_marks() >= 35
        and physics.get_practical_marks() >= 12
        and chemistry.get_theory_marks() >= 35
        and chemistry.get_practical_marks() >= 12
        and biology.get_theory_marks() >= 35
        and biology.get_practical_marks() >= 12
        and maths.get_theory_marks() >= 35
        and maths.get_practical_marks() >= 12
        and english.get_theory_marks() >= 35
        and english.get_practical_marks() >= 12
        and kannada.get_theory_marks() >= 35
        and kannada.get_practical_marks() >= 12
    ):
        print("OVERALL RESULT: PASS")
    else:
        print("OVERALL RESULT: FAIL")

    print("\nREPORT CARD GENERATED SUCCESSFULLY!")

else:
    print("\nReport card cannot be generated.")
    print("Please enter the correct roll number.")
    
    
    
