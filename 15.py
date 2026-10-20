#::::::::::::MENUE DRIVEN PROGRAMS::::::::::::::
def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def menu():
    print("\n SIMPLE CALCULATOR")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Exit")


while True:
    menu()  # Displays the menu to the user
    choice = int(input("Enter your choice (1 - 4): "))

    if choice == 4:
        print("Exiting the calculator")
        break
    elif choice in {1, 2, 3}:
        a = int(input("ENTER FIRST NUMBER: "))
        b = int(input("ENTER SECOND NUMBER: "))

        if choice == 1:
            print("Addition:", add(a, b))
        elif choice == 2:
            print("Subtraction:", sub(a, b))
        elif choice == 3:
            print("Multiplication:", multiplication(a, b))
    else:
        print("Invalid choice. Please select a valid choice.")


### BANKING SYSTEM:::::
def bank_menu():
    print("\n1. Deposit money\n2. Withdraw money\n3. Check balance\n4. Exit")


balance = 0

while True:
    bank_menu()
    choice = int(input("ENTER YOUR CHOICE: "))

    if choice == 4:
        print("Exiting from system, Thank You!!")
        break
    elif choice in {1, 2, 3}:
        if choice == 1:
            deposit = int(input("Deposit your amount please: "))
            balance += deposit
            print(f"Successfully deposited: {deposit}")

        elif choice == 2:
            withdraw = int(input("Enter your amount to withdraw: "))
            if withdraw <= balance:
                balance -= withdraw
                print("Withdrawn amount:", withdraw)
            else:
                print("Insufficient balance!")

        elif choice == 3:
            print("Balance:", balance)
    else:
        print("Invalid choice. Please select a valid choice.")
