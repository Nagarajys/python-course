# Armstrong number  WHILE CONCEPT
num = int(input("Enter a number: "))

temp = num
digits = len(str(num))
total = 0

while temp > 0:
    digit = temp % 10
    total = total + (digit ** digits)
    temp = temp // 10

if total == num:
    print("Armstrong Number")
else:
     print("Not an Armstrong Number")   
     
     
     # ARM STRONG NUMBER ANDRE PRATHI DIGIT DHU POWER ( ANDRE A NUMBER LENGTH YAST EDHYAST NA POWER MADBEKU)
     # POWER MADI BANDIRO NUMBER A NUMBER GAY EQUAL AGIRBEKU EX: 153 = 153 ETHARA               
    