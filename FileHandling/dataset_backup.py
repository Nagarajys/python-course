import shutil

try:
    shutil.copy("training_data.txt", "training_data_backup.txt")
    print("file copied successfully!")
except OSError as error:
    print("file not copied", {error})
