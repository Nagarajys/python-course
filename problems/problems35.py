 # Guess the Secret Number (break)  WHILE CONCEPT
secret_number = 27
while True:
    entered_number = int(input("enter a number"))
    if secret_number == entered_number:
        print("Correct! You guessed it.")
        break
    else:
        print("wrong number", "try again")