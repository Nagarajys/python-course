import logging

logging.basicConfig(
    filename="training_errors.log",
    level=logging.ERROR,
    format=" %(levelname)s : %(message)s",
)
try:
    with open("ai_training_data.csv", "r", encoding="utf-8") as file:
        file.read()

except FileNotFoundError:
    print("DATA SET NOT found ")
    logging.error(" data set loading failed")


# FILE PROCESSING WITH EXCEPTION HANDLING
try:
    with open("ai_model_report.txt", "r", encoding="utf-8") as file:
        accuracy = float(file.read())
        creater = file.read()
    if accuracy >= 85 and creater == "NAGARAJA YS":
        print("MODEL ACCEPTED")
    else:
        print("MODEL REJECTED")
except FileNotFoundError as error:
    print("FILE NOT FOUND:", error)
except ValueError as error:
    print("INVALID NUMBER :", error)


# FINAL PROBLEM ::::
import logging

logging.basicConfig(
    filename="training_errors.log",
    level=logging.ERROR,
    format="%(levelname)s:%(message)s",
)
try:
    with open("ai_model_report.txt", "r", encoding="utf-8") as file:
        data = {}
        for line in file:
            key, value = line.strip().split(":", 1)
            data[key.strip()] = value.strip()
    Creator = data["Creator"]
    Model = data["Model"]
    Accuracy = float(data["Accuracy"])
    Status = data["Status"]
    print("creator:", Creator)
    print("model:", Model)
    print("Accuracy:", Accuracy)
    print("Status:", Status)

    if Accuracy >= 85:
        print("MODEL  ACCEPTED")
    else:
        print("MODEL REJECTED")
except FileNotFoundError as error:
    print("FILE NOT FOUND:", error)
except ValueError as error:
    print("VALUE ERROR")
    logging.error("DATESET  LOADING FAILDED")
