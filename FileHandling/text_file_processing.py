from pathlib import Path

file_path = Path("ai_report.txt")
try:
    with file_path.open("r", encoding="utf-8") as file:
        count = 0
        for line in file:
            if "training" in line.lower():
                count = count + 1
    print("count of completed", count)

except FileNotFoundError:
    print("File doesn't exists !")
except OSError as error:
    print("file error", error)
