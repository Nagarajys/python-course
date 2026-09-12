# problems on OOP:
class student:
    def __init__(self, name):
        self.name = name


s1 = student("nagaraj")
print(s1.name)


class car:
    def __init__(self, brand):
        self.brand = brand


car1 = car("bmw")
car2 = car("thar roxx")
print(car1.brand)
print(car2.brand)


class mobile:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price


m1 = mobile("samsaung", "30k")
m2 = mobile("vivo", "25k")

print(m1.brand)
print(m1.price)
print(m2.brand)
print(m2.price)


class bike:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year


b1 = bike("ktm 390", 2007)
b2 = bike("royal enfield", 1998)
b3 = bike("gtr", 2014)

print(b1.brand)
print(b1.year)
print(b2.brand)
print(b2.year)
print(b3.brand)
print(b3.year)


class laptop:
    def __init__(self, name, ram, storage):
        self.name = name
        self.ram = ram
        self.storage = storage


l1 = laptop("asus tuf a15", "16gb", "512gb")
print(l1.name)
print(l1.ram)
print(l1.storage)


class phone:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


p1 = phone("samsaung", "2005")
p2 = phone("vivo", "2000")

print(p1.brand)
print(p1.model)
print(p2.brand)
print(p2.model)


class employe:
    def __init__(self, name, salry):
        self.name = name
        self.salry = salry


emp = employe("vikas", "50000")
print(emp.name)
print(emp.salry)


class bankaccount:
    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance


person1 = bankaccount("nagaraj", "9353132645")
person2 = bankaccount("subramanya", "6361273988")

print(person1.holder)
print(person1.balance)
print(person2.holder)
print(person2.balance)


class products:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


food = products("dhum biriyani", "299", "10")
print(food.name)
print(food.price)
print(food.quantity)


class book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


publisher = book("ENGINEERING WITH RAJ", "NAGARAJ")
print(publisher.title)
print(publisher.author)


class players:
    def __init__(self, name, score):
        self.name = name
        self.score = score


player1 = players("nagaraj", 100)
player2 = players("karthik", 99)
print(player1.name)
print(player1.score)
print(player2.name)
print(player2.score)


class rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth


obj = rectangle(10, 5)
area = obj.length * obj.breadth
print(area)


class circle:
    def __init__(self, radius):
        self.radius = radius


obj = circle(7)
area = 3.14 * obj.radius * obj.radius
print(area)


class employee:
    def __init__(self, monthly_salary):
        self.monthly_salary = monthly_salary


money = employee(200000)
annual_salary = money.monthly_salary * 12
print(annual_salary)


class product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


items = product("bmw", 500000)
if items.price > 1000:
    print("expensive")
else:
    print("affordable")


class player:
    def __init__(self, name, score):
        self.name = name
        self.score = score


p1 = player("nagaraj", 10)
p2 = player("sutejh", 8)
p3 = player("rahulla", 1)

highest = p1

if p2.score > highest.score:
    highest = p2

if p3.score > highest.score:
    highest = p3
print(highest.name)
print(highest.score)
