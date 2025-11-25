# sample 5 files

file = open("test.txt", "w")
file.write("Hello World")
file.close()

with open("test.txt", "w") as file:  # with op
    file.write("Hello World")

with open("test.txt", "r") as file:
    print(file.read())

with open("test.txt", "a") as file:
    file.write("\nHello World")

with open("test.txt", "r") as file:
    print(file.read())
