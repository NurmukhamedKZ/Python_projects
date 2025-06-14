with open("text1.md", "r") as file:
    content = file.read()
    print(content)

content = "bye"

with open("text1.md", "a") as file:
    file.write(content)