"""1. Important Points 📝
FileNotFoundError occurs when the requested file cannot be found.
Use try-except to prevent your program from crashing because of a missing file.
with open() automatically closes the file.
Exception order matters: Handle FileNotFoundError before OSError,
because FileNotFoundError is a subclass of OSError."""

try:
    with open("ai_training_data.csv", "r", encoding="utf-8") as file:
        data = file.read()
        print("AI DATASET PROCESSING COMPLETED")
        print(data)
except FileNotFoundError as error:
    print("error:", error)
except OSError as error:
    print("file error:", error)


# problemmsss
try:
    with open("model_status.txt", "r", encoding="utf-8") as file:
        data = file.read()

    if data.strip():
        if "Model:" in data and "Accuracy:" in data:
            print("VALID MODEL REPORT")
            print(data)
        else:
            print("INVALID MODEL REPORT..")
    else:
        print("THE FILE IS EMPTY")
except FileNotFoundError as error:
    print("FILE NOT FOUND:", error)
except OSError as error:
    print("FILE ERROR:", error)
