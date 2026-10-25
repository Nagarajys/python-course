import csv

data = [
    ["Model", "Accuracy", "Status"],
    ["CNN", "95", "Completed"],
    ["RNN", "91", "Completed"],
    ["ANN", "88", "Testing"],
]
try:
    with open("model_results.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        print(writer.writerow(["Model", "Accuracy", "Status"]))
        print(writer.writerows(data))
    print("CSV FILE CREATED SUCESSFULLT")
except OSError as error:
    print("FILE ERROR:", error)
