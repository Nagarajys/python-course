with open("ai_model.txt", "r") as file:
    content = file.read()
    print(content)
print("file closed automatically")
print(file.closed)
