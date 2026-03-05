name = "Joyi"
age = 20

print(f"My name is {name} and I am {age}")

a = 5
b = 10

print(f"Sum is {a+b}")

pi = 3.14159
print(f"Pi value: {pi:.2f}")

### Debugging trick

x = 10

print(f"{x=}")

## alignment formatting

name = "Joyi"

print(f"{name:>10}")
print(f"{name:<10}")
print(f"{name:^10}")    ## centre align

## For Ai/ML

accuracy = 0.92345

print(f"Model accuracy: {accuracy:.2%}")