with open("readme.md", "r") as file:
    content = file.read()
    print(content)

content = "bye"

with open("readme.md", "a") as file:
    file.write(content)
    
# this is a comment

a = 10

