# creating folder using directoryy:::
from pathlib import Path

folder_path = Path("AI_Training_Results")

try:
    folder_path.mkdir()
    print("Folder created successfully!")

except FileExistsError:
    print("Folder already exists!")

except OSError as error:
    print("Folder creation failed:", error)

# Check whether it is a directory
if folder_path.is_dir():
    print("Directory verified successfully!")

    # List items inside the directory
    print("Items inside the folder:")
    for item in folder_path.iterdir():
        print("created file name:", item.name)

        if item.is_file():
            content = item.read_text()
            print(content)

else:
    print("Directory not found!")
