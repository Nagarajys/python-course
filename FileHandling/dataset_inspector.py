# Problem 17 — AI Dataset Inspector
from pathlib import Path

file_path = Path("training_data.txt")
if file_path.is_file():
    print("FILE_NAME:", file_path.name)
    print("EXTENSION:", file_path.suffix)
    print("SIZE:", file_path.stat().st_size, "bytes")
    print("PARENT DIRECTORY:", file_path.parent)
else:
    print("dataset not found!!")

# PROBLEM 19 — AI Dataset Renamer
from pathlib import Path

try:
    file_path = Path("training_data_backup.txt")
    file_path.rename("final_ai_dataset.txt")
    print("FILE RENAMED SUCCESSFULLY")
except OSError as error:
    print("FILE RENAME FAILED", error)
