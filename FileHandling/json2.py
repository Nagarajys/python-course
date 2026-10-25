# FILE ENCODING - UTF-8

try:
    with open("ai_notes.txt", "w", encoding="utf-8") as file:
        file.write("AI Engineer\n")
        file.write("Artificial Intelligence\n")
        file.write("ಕೃತಕ ಬುದ್ಧಿಮತ್ತೆ\n")

    print("File written successfully!")

    with open("ai_notes.txt", "r", encoding="utf-8") as file:
        content = file.read()

    print("\nFile Content:")
    print(content)

except OSError as error:
    print("FILE ERROR:", error)
