from pathlib import Path

file_path = Path("AI_Training_Results/training_log.txt")
try:
    with file_path.open("r", encoding="utf-8") as file:
        for line in file:
            print(line, end="")
except FileNotFoundError:
    print("file not found")
except OSError as error:
    print("Error:", error)
