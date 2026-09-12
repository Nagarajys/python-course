class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


student1 = Student("Nagaraj", 18)
student2 = Student("Rahul", 19)

student1.display()
student2.display()


'''Student       → Class
Student(...)  → Create object
__init__()    → Automatically runs
self          → Current object
name          → Received value
self.name     → Current object's name
self.name=name → Store name inside object'''


'''Student → class
Student("Nagaraj", 18) → creates the object
student1 → that object-na reference/name
self → currently created object
self.name → that object's name data
self.age → that object's age data'''