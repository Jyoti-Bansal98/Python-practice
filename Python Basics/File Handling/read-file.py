## opening a file
file = open("test.txt", "r")
content = file.read()
print(content)
file.close()

## read() → pura data ek string me deta hai

# line by line
file = open("test.txt", "r")

for line in file:
    print(line)

file.close()

## using WITH
with open("test.txt", "r") as file:
    content = file.read()
    print(content)

# read line by line using WITH
with open("test.txt", "r") as file:
    for line in file:
        print(line)

# read lines as LIST using WITH
with open("test.txt", "r") as file:
    lines = file.readlines()
print(lines)


