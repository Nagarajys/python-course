from abc import ABC, abstractmethod

# ---------------- STUDENT ----------------


class Student:
    def __init__(self, candidate_name, roll_number):
        self.candidate_name = candidate_name
        self.roll_number = roll_number

    def fetch_details(self):
        pass


class Details(Student):
    def __init__(self, candidate_name, roll_number, exam_type):
        super().__init__(candidate_name, roll_number)
        self.status = False
        self.exam_type = exam_type

    def fetch_details(self):
        self.status = True

        print("Candidate Name:", self.candidate_name)
        print("Roll Number:", self.roll_number)
        print("Exam Type:", self.exam_type)
        print("Status: ACTIVE")

    def show_status(self):
        print("EXAM TYPE:", self.exam_type)


# ---------------- ABSTRACT EXAM ----------------


class Exams(ABC):

    def __init__(self):
        self.__questions = []
        self.__answers = []

    # Controlled way to add question and correct answer
    def add_question(self, question, answer):
        self.__questions.append(question)
        self.__answers.append(answer)

    # Controlled access to questions
    def get_questions(self):
        return self.__questions

    # Controlled access to correct answers
    def get_answers(self):
        return self.__answers

    @abstractmethod
    def evalvation(self, candidate_answers):
        pass


# ---------------- MCQ EXAM ----------------


class MCQexam(Exams):

    def __init__(self):
        super().__init__()

        self.add_question("What is RAM?", "random access memory")

        self.add_question("What is the sum of 2026?", 10)

        self.add_question("What is the full form of JEE?", "joint entrance exam")

    def evalvation(self, candidate_answers):

        marks = 0

        questions = self.get_questions()
        answers = self.get_answers()

        for i in range(len(answers)):

            print("Question:", questions[i])
            print("Candidate Answer:", candidate_answers[i])

            if candidate_answers[i] == answers[i]:
                print("Correct Answer")
                marks += 1
            else:
                print("Wrong Answer")

            print()

        print("MCQ FINAL MARKS:", marks)


# ---------------- CODING EXAM ----------------


class Codingexam(Exams):

    def __init__(self):
        super().__init__()

        self.add_question(
            "What is a variable?", "it is symbolic link used to store data"
        )

        self.add_question(
            "What is Fibonacci series?", "it is sequence of sum of 2 preceding numbers"
        )

    def evalvation(self, candidate_answers):

        marks = 0

        questions = self.get_questions()
        answers = self.get_answers()

        for i in range(len(answers)):

            print("Question:", questions[i])
            print("Candidate Answer:", candidate_answers[i])

            if candidate_answers[i] == answers[i]:
                print("Correct Answer")
                marks += 5
            else:
                print("Wrong Answer")

            print()

        print("CODING FINAL MARKS:", marks)


# ---------------- PRACTICAL EXAM ----------------


class Practicalexam(Exams):

    def __init__(self):
        super().__init__()

        self.add_question("What is maximum pH of acid?", 1)

        self.add_question("What is maximum pH of base?", 14)

    def evalvation(self, candidate_answers):

        marks = 0

        questions = self.get_questions()
        answers = self.get_answers()

        for i in range(len(answers)):

            print("Question:", questions[i])
            print("Candidate Answer:", candidate_answers[i])

            if candidate_answers[i] == answers[i]:
                print("Correct Answer")
                marks += 1
            else:
                print("Wrong Answer")

            print()

        print("PRACTICAL FINAL MARKS:", marks)


# ---------------- STUDENT DETAILS ----------------

student1 = Details("nagaraj", 202679543, "MCQ Exam")

student2 = Details("sutej", 202674965, "Coding Exam")

student3 = Details("satish", 8088331801, "Practical Exam")


# ---------------- FETCH STUDENT DETAILS ----------------

student1.fetch_details()

print()

student2.fetch_details()

print()

student3.fetch_details()

print()


# ---------------- CREATE EXAM OBJECTS ----------------

mcq = MCQexam()

coding = Codingexam()

practical = Practicalexam()


# ---------------- CANDIDATE ANSWERS ----------------

mcq_answers = ["random access memory", 10, "joint entrance exam"]

coding_answers = [
    "it is symbolic link used to store data",
    "it is sequence of sum of 2 preceding numbers",
]

practical_answers = [1, 14]


# ---------------- PROCESS MULTIPLE EXAMS ----------------

exam_records = [
    (mcq, mcq_answers),
    (coding, coding_answers),
    (practical, practical_answers),
]


for exam, candidate_answers in exam_records:
    print("\n----------------------------")
    exam.evalvation(candidate_answers)


"""Q25 — Smart Parking Management System

Design a Smart Parking Management System using Python OOP.

A parking facility has different types of vehicles:

Bike
Car
Truck

Each vehicle should have its own way of calculating parking charges.

The system should:

Store vehicle details such as number/type.
Allow a vehicle to enter the parking area.
Allow a vehicle to exit the parking area.
Calculate the parking fee based on the vehicle type and parking duration.
Keep the currently parked vehicle information protected from direct external modification.
Process multiple parked vehicles together using a list + loop.
Display each vehicle's details and final parking fee.
Use all four OOP pillars.
Demonstrate polymorphism when calculating parking charges."""

from abc import ABC, abstractmethod


# Parent class: stores vehicle details (Encapsulation)
class vehical:
    def __init__(self, number, type, duration):
        self.__number = number
        self.__type = type
        self.__duration = duration

    # Getter methods to access private variables
    def get_number(self):
        return self.__number

    def get_type(self):
        return self.__type

    def get_duration(self):
        return self.__duration

    def details(self):
        pass


# Stores vehicle information and manages parking status (Inheritance)
class information(vehical):
    def __init__(self, number, type, duration, vehical_type):
        super().__init__(number, type, duration)
        self.status = False
        self.vehical_type = vehical_type

    # Displays vehicle details
    def details(self):
        print("\nVEHICLE DETAILS")
        print("Vehicle Number:", self.get_number())
        print("Vehicle Model:", self.get_type())
        print("Vehicle Type:", self.vehical_type)
        print("Parking Duration:", self.get_duration(), "hours")

    # Allows vehicle to enter parking
    def enter_parking(self):
        if not self.status:
            self.status = True
            print(self.get_number(), "entered parking successfully")
        else:
            print(self.get_number(), "is already parked")

    # Displays parking status
    def show_status(self):
        if self.status:
            print("Status: Currently Parked")
        else:
            print("Status: Not Parked")

    # Allows vehicle to exit parking
    def exit_parking(self):
        if self.status:
            self.status = False
            print(self.get_number(), "exited parking successfully")
        else:
            print(self.get_number(), "is not currently parked")


# Abstract class: defines parking-charge calculation
class parking_charge(ABC):
    def __init__(self, charge_per_hour, vehicle):
        self.charge_per_hour = charge_per_hour
        self.vehicle = vehicle

    @abstractmethod
    def calculate_charge(self):
        pass


# Bike parking charge
class Bikes(parking_charge):
    def calculate_charge(self):
        if not self.vehicle.status:
            print("Bike is not parked. Cannot calculate parking charge.")
            return

        final_charge = self.vehicle.get_duration() * self.charge_per_hour

        print("\nBIKE PARKING BILL")
        print("Vehicle Number:", self.vehicle.get_number())
        print("Duration:", self.vehicle.get_duration(), "hours")
        print("Hourly Charge: ₹", self.charge_per_hour)
        print("FINAL CHARGE: ₹", final_charge)
        return final_charge


# Car parking charge
class Cars(parking_charge):
    def calculate_charge(self):
        if not self.vehicle.status:
            print("Car is not parked. Cannot calculate parking charge.")
            return

        final_charge = self.vehicle.get_duration() * self.charge_per_hour

        print("\nCAR PARKING BILL")
        print("Vehicle Number:", self.vehicle.get_number())
        print("Duration:", self.vehicle.get_duration(), "hours")
        print("Hourly Charge: ₹", self.charge_per_hour)
        print("FINAL CHARGE: ₹", final_charge)
        return final_charge


# Truck parking charge
class Trucks(parking_charge):
    def calculate_charge(self):
        if not self.vehicle.status:
            print("Truck is not parked. Cannot calculate parking charge.")
            return

        final_charge = self.vehicle.get_duration() * self.charge_per_hour

        print("\nTRUCK PARKING BILL")
        print("Vehicle Number:", self.vehicle.get_number())
        print("Duration:", self.vehicle.get_duration(), "hours")
        print("Hourly Charge: ₹", self.charge_per_hour)
        print("FINAL CHARGE: ₹", final_charge)
        return final_charge


# Creating vehicle information objects
VI1 = information("KA143730", "KTM 390", 3, "bike")
VI2 = information("KA183730", "Lamborghini", 5, "car")
VI3 = information("KA153730", "Tata", 24, "truck")


# Storing vehicle information together
vehicles_information = [VI1, VI2, VI3]


# Display details and allow parking entry
for vehicle in vehicles_information:
    vehicle.details()
    vehicle.enter_parking()
    vehicle.show_status()


# Creating parking-charge objects
BIKES = Bikes(100, VI1)  # ₹100 per hour
CARS = Cars(150, VI2)  # ₹150 per hour
TRUCKS = Trucks(99, VI3)  # ₹99 per hour


# Storing all parking-charge objects in one list
all_vehicles = [BIKES, CARS, TRUCKS]


# Calculate charges using polymorphism
print("\n========== PARKING CHARGES ==========")

for vehicle_charge in all_vehicles:
    vehicle_charge.calculate_charge()


# Allow vehicles to exit after charge calculation
print("\n========== VEHICLE EXIT ==========")

for vehicle in vehicles_information:
    vehicle.exit_parking()
    vehicle.show_status()
