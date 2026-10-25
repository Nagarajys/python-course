with open("config.txt", "r") as file:
    print("initial status:", file.closed)
    content = file.read()
    print(content)
print("final status:", file.closed)
