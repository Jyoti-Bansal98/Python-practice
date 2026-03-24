## append

fruits = ['apple','banana']
fruits.append('mango')
print(fruits)

numbers = [1, 2]
numbers.append([3,4])
print(numbers)   ## [3,4] become one element as list can only add one element at a time.

numbers = [1,2]
numbers = numbers + [3,4]
print(numbers)

## real use case

numbers = []

for i in range(10):
    numbers.append(i)
print(numbers)

nums = [10,20,30]

nums = nums + [40,50]
print(nums)


## insert

numbers = [1, 2, 3]
numbers.insert(1, 10)
print(numbers)

nums = [1,2,3]
nums.insert(10, 5)
print(nums)

nums = [10, 20, 30]

nums.insert(1,15)
nums.insert(0,5)
print(nums)


