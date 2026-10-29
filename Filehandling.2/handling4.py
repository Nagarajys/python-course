# problem jsonnn
import json

try:
    with open("ai_results.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    print(data["model"])
    print(data["accuracy"])
except FileNotFoundError as error:
    print("FILE NOT FOUND:", error)
except json.JSONDecodeError as error:
    print("INVALID JSON:", error)
except OSError as error:
    print("FILE ERORR:", error)


##problems::
class InvalidDataError(Exception):
    pass


data_set = 0
try:
    if data_set <= 0:
        raise InvalidDataError("DATA SET MUST BE GRATER THAN ZERO")
    print("DATA SET IS VALID")
except InvalidDataError as error:
    print("validation error:", error)
