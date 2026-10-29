from pathlib import Path

file_path = Path("ai_dataset.csv")
try:
    if file_path.exists():
        print("DATASET FOUND")
        print("file_size:", file_path.stat().st_size(), "bytes")

        with open("ai_dataset.csv", "r", encoding="utf-8") as file:
            data = file.read()
            print("dataset contents:")
            print(data)
    else:
        print("dataset not found")
except OSError as error:
    print("file error:", error)

##Student Records Management System
try:

    with open("students.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
        print("".join(lines))
        total = 0
        for line in lines:
            total = total + 1
        print(total)
except FileNotFoundError as error:
    print("file not found:", error)

# STUDENT MARKS ANALYZER:
from pathlib import Path

file_path = Path("students.txt2")
try:
    with open("students.txt2", "r", encoding="utf-8") as file:
        lines = file.readlines()
        total_marks = 0
        count = 0
        for line in lines:
            if line.startswith("Marks:"):
                marks = int(line.split(":")[1].strip())
                total_marks += marks
                count = count + 1
        if count > 0:
            average_marks = total_marks / count
            print("total marks:", total_marks)
            print("average_marks:", average_marks)

        else:
            print("data not found")
except FileNotFoundError as error:
    print("file not found :", error)
