"""PRACTICAL PROBLEM 10 — AI MODEL TRAINING REPORT
Scenario
You are developing an AI model and need to save its training report."""

file = open("training_report.txt", "w")
data = [
    "Project: AI Disease Detection\n"
    "Dataset: 5000 Records\n"
    "Accuracy: 94.5%\n"
    "Status: Model Training Completed"
]
file.writelines(data)
file.close()
print("AI training report saved successfully!.")
