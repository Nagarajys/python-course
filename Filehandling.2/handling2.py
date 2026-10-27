try:
    with open("model_report.txt", "w", encoding="utf-8") as file:
        file.write("AI MODEL TRAINING COMPLETED")
    print("REPORT SAVED SUCCESSFULLY")
except FileNotFoundError as error:
    print("ERROR:", error)
except OSError as error:
    print("FILE ERROR:", error)
