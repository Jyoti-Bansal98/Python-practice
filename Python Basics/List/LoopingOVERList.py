### LOOPING OVER LIST

numbers = [10, 20, 30, 40]

for num in numbers:
    print(num)


## Using Index

numbers = ['@','$','%','&']

for i in range(len(numbers)):
    print(numbers[i])


## using enumerate

numbers = [10, 20, 30]

for index, value in enumerate(numbers):
    print(index, value)


## modifying while looping

numbers = [1,2,3,4]
for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2 

print(numbers)


## Looping with condition

numbers = [1,2,3,4,5,6]

for num in numbers:
    if num % 2 == 0:    
        print(num)     


## creating new list using looping
  
numbers = [1,2,3,4]
squares = []

for num in numbers:
    squares.append(num*num)     ## This is very common in ML preprocessing.
                           
print(squares)


## Loop Through Strings Inside List

fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(fruit.upper())


numbers = [5,10,15,20]

# print each number
# print number * 2

for i in range(len(numbers)):
    print(numbers[i], numbers[i]*2)

