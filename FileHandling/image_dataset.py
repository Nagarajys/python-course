import csv

try:
    with open("ai_dataset.csv", "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header

        for row in reader:
            print("Image:", row[0], "| Label:", row[1])

except FileNotFoundError:
    print("CSV file not found!")

except OSError as error:
    print("File error:", error)
