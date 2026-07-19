# problem : 27 - E-Commerce Discount System
amount = int(input("amount: "))
discount = int(input("discount (percent): "))

if amount >= 10000 and discount == 20:
    discount_amount = amount * discount / 100
    final_amount = amount - discount_amount
    print("discount amount:", discount_amount)
    print("final amount:", final_amount)
    
    
elif 5000<=amount<=9999 and discount == 10:
    discount_amount = amount*discount/100
    final_amount = amount - discount_amount
    print("discount_amount:", discount_amount)
    print("final_amount:", final_amount)
    
elif 2000<=amount<=4999 and discount ==5:
    discount_amount = amount*discount/100
    final_amount = amount - discount_amount
    print("discount_amount:", discount_amount)
    print("final_amount:", final_amount)
elif amount<2000:
    print("no discount")
else:
    print("pay full cash")