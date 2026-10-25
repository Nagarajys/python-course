import json

# 1. ACCESS INDIVIDUAL VALUES
try:
    with open("ai_model.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    print("\n--- AI MODEL DETAILS ---")
    print("Model:", data["model"])
    print("Accuracy:", data["accuracy"])
    print("Epochs:", data["epochs"])
    print("Training Completed:", data["training completed"])
    print("Layers:", data["layers"])

except FileNotFoundError:
    print("ERROR: ai_model.json not found!")

except json.JSONDecodeError as error:
    print("INVALID JSON:", error)

except OSError as error:
    print("FILE ERROR:", error)


# 2. CREATE JSON FILE IF IT DOES NOT EXIST
try:
    with open("ai_project.json", "x", encoding="utf-8") as file:
        data = {
            "project": "AI Image Classifier",
            "dataset_size": 5000,
            "accuracy": 97.2,
            "completed": True,
            "algorithms": ["CNN", "RNN", "ANN"],
        }

        json.dump(data, file, indent=4)

    print("\nAI project JSON file created successfully!")

except FileExistsError:
    print("\nai_project.json already exists. Existing data preserved.")

except OSError as error:
    print("FILE ERROR:", error)


# 3. UPDATE EXISTING JSON FILE
try:
    # Read existing data
    with open("ai_project.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    # Update only the required values
    data["accuracy"] = 99.1
    data["completed"] = False
    data["version"] = 2

    # Save the complete updated dictionary ONCE
    with open("ai_project.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    print("JSON file updated successfully!")

    # Display the updated information
    print("\n--- UPDATED AI PROJECT ---")
    print(json.dumps(data, indent=4))

except FileNotFoundError:
    print("ERROR: ai_project.json not found!")

except json.JSONDecodeError as error:
    print("INVALID JSON:", error)

except OSError as error:
    print("FILE ERROR:", error)
