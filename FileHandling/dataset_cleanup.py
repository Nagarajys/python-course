from pathlib import Path

try:
    file_path = Path("temporary_dataset.txt")
    if file_path.is_file():
        file_path.unlink()
        print("file deleted succsessfully")
    else:
        print("file not found")
except OSError as error:
    print("file deletion failed", error)
