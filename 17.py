# TOPIC : ERRORS AND EXCEPTION HANDLINGGG::::::
a = int(input("a:"))
b = int(input("b:"))
try:
    print(a / b)  # ee operation possible edre matra print madutte

except (
    Exception
) as problem:  # operatio possible illa andre Exception na except madko problem roopa dalli
    print("Error banthu:", {problem})  # addunay print madu except madiro problem naa

else:
    print("Yanu error barllila")  #  in case try work adre eee line excecute agutte

finally:  # finaal y edu eeeror barli athva bardhe erli yan adru work agutte
    print("program ended! , eroor bandru barlila andru nan care madalla")


# EXAMPLES OF EXCEPTIOON HANDLING::::;
# 1.CATCHING DIVISION BY ZEROOOOOO::
try:
    a = int(input("enter a number:"))
    print(10 / a)
except (
    ZeroDivisionError
):  # ee zerodivisionerro evaylla EXCEPTION ANNO PARRRENT CLASS NA SUBLCASES KANO
    print("you can't  divide by zero!!")
else:
    print("yes you can , bcz there is no error")


# EXAMPLE 2::HANDLING MULTIPLEEEE EXCEPTIONSSS::
try:
    num = int(input("enter a number:"))
    result = 10 / num
    print("Result:", result)


except (
    ZeroDivisionError
):  # andre navu subclass na ddirect implement madthidivi if nanu 10/0 madudre
    # adu direct agi zerodivisionerror na accept madkolte
    print("Cannot divide by zero")


except (
    ValueError
):  # andre navu subclass na ddirect implement madthidivi , if nanu number badlu
    # string kotre addhu value error  na accept madkoluttee
    print("please enter a valid number , never enter a string type here")


else:  # if namma try yalladru true agidre edh excute aguute
    print("yav error kuda barudilla a a a a a a a a a a a a a a a a a")


#### RAISING EXCEPTIONSSSS:::::::
try:
    boy = input("WHO DO YOU WANT TO MARRY:")
    if boy != "Sutej":  # boy yalladru sutej agilla andre exception raose maduuu
        raise Exception("You can only marry sutej , so select him - ")

except Exception as error:  # aa raise agiro exception na except maduuu
    print("error:", {error})

else:  # yalaldru boy sutej ayy agidre marry agu anta
    print("YES SUTEJ IS READY TO MARRY YOU")
