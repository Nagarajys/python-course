# OOP -  INTRODUCTION TO OOP CONCEPTS AND CLASSES AND OBJECTS:
# some problem:

from os import name


class cars:
    pass
car1 = cars()
car2 = cars()


class mobile:
    pass
phone1 = mobile()
phone2 = mobile()
phone3 = mobile()


class student:
    pass
s1 = student()
s2 = student()
s3 = student()

class teacher:
    pass
t1 = teacher()
t2 = teacher()
t3 = teacher()

class subject:
    pass
sub1 = subject()
sub2 = subject()
sub3 = subject()

class animal:
    pass
dog = animal()
cat = animal()
rat = animal()


class bus():
    pass
ksrtc = bus()
bmtc = bus()
airavata = bus()

 
#CONSTRUCTOR , SELFKEYWORD AND OPTIONAL PARAMERTER:
class classname:
    def __init__(self,parameter1,parameter2):#init is constructor when class iscreating a object
        #init will recive  a block of code to construct
        
        self.attribute1 = parameter1# self andre nanna(mine) 
        self.attribute2 = parameter2
        


class human:
    def __init__(self,name,age):
        print("constructor is called", name)
        self.name = name# these are all object variables
        self.age = age
        
    def walk(self):
        print(f"{self.name} is walking")
        
c = human("chandan",22)
d = human("dacchu",20)# object helkotide eddu nandu anta nana attributes 

human.walk(d) # human anno class alli walk anno method edde adhake nanu d anno object na kalsthini



#accesing the data:
class students:
    def __init__(self,name):
        self.name = name
s1 = students("nagaraj")
s2  =students("rahulla")
s3 = students("russel")

print(s1.name)
print(s2.name)
print(s3.name)



class car:
    def __init__(self, brand , colour , price):
        self.brand = brand
        self.colour = colour
        self.price = price
car1  = car("bmw","black" , "500000")
car2 = car("lamborghini", "green" , "77007070707")
car3 = car("oddi" , "white" , "4500000")

print(car1.brand)
print(car1.colour)
print(car1.price)
print(car2.brand)
print(car2.colour)
print(car2.price)
print(car3.brand)
print(car3.colour)
print(car3.price)


class members():
    def __init__(self , name =  "unknown"):
        self.name = name
        
m1  = members("vani")
m2 = members()

print(m1.name)
print(m2.name)

# multiple attributes:
class laptop:
    def __init__(self,name,processor,ram,graphics):
        self.name = name
        self.processor = processor
        self.ram = ram
        self.graphics = graphics
        
lap1 = laptop("asus a 15", "ryzen7" , "16gb ram", "rtx3050")
print(lap1.name)
print(lap1.processor)
print(lap1.ram)
print(lap1.graphics)


