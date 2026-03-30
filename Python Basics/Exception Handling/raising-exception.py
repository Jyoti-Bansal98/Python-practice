age = int(input())

if age < 0:
    raise ValueError("Age cannot be negative")
print(age)

