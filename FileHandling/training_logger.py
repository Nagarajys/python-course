try:
    with open("training_log.txt", "a") as file:
        file.write("\nAI  MODEL TRAINING COMPLETED")
    print("training log updated successfully")
except OSError as error:
    print("FILE OPERATION FAILED ", error)


from pathlib import Path

file_path = Path("training_data.txt")

if file_path.is_file():
    print("File name:", file_path.name)
    print("Extension:", file_path.suffix)
    print("File size:", file_path.stat().st_size, "bytes")
else:
    print("File not found!")
