file = open("notes.txt", "r")
contents = file.readlines()
print(contents)
file.close()


# write
file = open("students.txt", "a")
file.write(" \nHE IS A FREE FIRE PLAYER 4 YEARS BACK")
file.write("\nchandan bro is my real teacher")
file.write("\n nagaraj bro is my inspirationnn")

# create x if file does not exist:
file = open("employes.txt", "a")
file.write("\n russel bro")
file.close()

# mixing file handling and excepting handling:

file = None
try:
    file = open("employes.txt", "x")
    file.write("\n raja")
except Exception as error:
    print("Error:", {error})
finally:
    if file:
        file.close()
        print("FINALLY FILE CLOSED")
## using with to close the file automatically ::
students = ["chandana 1", "darshana1", "nagaraj1"]
with open("class1.txt", "w") as file:
    for student in students:
        file.write(f"{student}\n")

##READING  FILE AND PROCESSING EACH LINEEEE
with open("students.txt", "r") as file:
    for line in file:
        print("about them", line.strip())
