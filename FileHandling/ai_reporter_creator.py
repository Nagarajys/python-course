try:
    with open("model_reporter.txt", "x") as file:
        data = [
            "Project: AI Image Classifier\n",
            "Dataset: 5000 Images\n",
            "Status: Training Completed\n",
        ]
        file.writelines(data)
        print("FILE CREATED SUCCESSFULLY")
except FileExistsError as error:
    print("ERROR: FILE ALREADY EXISTS", {error})

