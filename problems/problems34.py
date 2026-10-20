# mini login system  WHILE CONCEPT
username =input("enter your name=")
Password = "python123"
attempt = 3
while attempt>0:
    entered_password =input("enter your password=")
    if Password == entered_password:
        print("welcome admin")
        break
    
    else:
        attempt = attempt-1
        print("wrong password")
        
    if attempt ==0:
        print("account locked")
        