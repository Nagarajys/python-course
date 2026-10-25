from pathlib import Path

file_path = Path("training_data.txt")

if file_path.is_file() == True:
    print("Dataset file found")
else:
    print("Dataset file not found")
print(file_path.name)
print(file_path.suffix)
