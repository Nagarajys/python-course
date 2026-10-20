#WHILE CONCEPT
balance = 90000
pin = 3730
while True:
    print("\n----ATM MENU----") # \N USED TO LEAVE A LINE BETWEEN 2 LINES
    print("1.check balance")
    print("2.deposit ")
    print("3.withdraw")
    print("4.exit")
    print("5.change pin")
    
    choice = int(input("enter your choice="))
    if choice == 1:
        print("balance=", balance)

    elif choice == 2:
        amount = int(input("enter amount = "))
        if amount > 0:
            balance = amount + balance
            print("successfully deposited your amount" , balance)
        else:
            print("enter a positive amount")

    elif choice == 3:
        amount = int(input("enter withdraw amount"))
        if amount <= balance and amount > 0:
            balance = balance - amount
            print("please collect your cash")
            print("remaining balance=", balance)
        elif amount <= 0:
            print("enter a positive amount")
        else:
            print("insufficient balance")

    elif choice == 4:
        print("exiting...")
        break
    
    elif choice == 5:
        old_pin = int(input("enter your pin"))
        if old_pin == pin:
            new_pin = int(input("enter new pin-"))
            pin = new_pin
            print("successfully changed pin:", new_pin)
        else:
            print("invalid pin")
    else:
        print("invalid choice")
        
        

        
    

    










