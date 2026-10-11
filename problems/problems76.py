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
