# OOP -  INTRODUCTION TO OOP CONCEPTS AND CLASSES AND OBJECTS:
# some problem:

from os import name


class car:
    pass
car1 = car()
car2 = car()


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




