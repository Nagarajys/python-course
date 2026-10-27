try:
    with open("model_status.txt", "r", encoding="utf-8") as file:
        data = file.read()
    if data.strip():
        print(data)
    else:
        print("MODEL STATUS FILE IS EMPTY")
except FileNotFoundError as error:
    print("file not found", error)
except OSError as error:
    print("File error", error)


# problem:
try:
    with open("ai_training_report.txt", "a", encoding="utf-8") as file:

        file.write("Status: Training completed\n")

    print("REPORT SAVED SUCCESSFULLY")
except FileExistsError as error:
    print("FILE ALREADY EXISTS:", error)
except FileNotFoundError as error:
    print("FILE NOT FOUND:", error)
except OSError as error:
    print("FILE ERORR:", error)
