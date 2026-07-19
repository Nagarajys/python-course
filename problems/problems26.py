# problem: 26 -Student Scholarship System
marks = (int(input("marks>=")))
income = (int(input("income<=")))
if marks >=90 and income <=200000:
    print("100% scolarship")
elif marks >=80 and income <= 500000:
    print("80% scolarship")
elif marks >=60 and income <= 100000:
    print("50% scolarship")
else:
    print("you are not al;lowed for scolarship")