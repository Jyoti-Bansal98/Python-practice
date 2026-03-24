## remove

numbers = [10, 20, 30, 40]
numbers.remove(30)
print(numbers)

nums = [1, 2, 3, 2, 4]
nums.remove(2)   ## remove just remove the first occurance of that value.  
print(nums)   

fruits = ["apple", "banana", "mango"]
# fruits.remove("papaya")  ## if value doesnot exist than python will give error.
# print(fruits)

## safe way

nums = ['harsh','adu','ritik','joyi']

if 'harsh' in nums:
    nums.remove('harsh')

print(nums)

nums = [10,20,30,40,50]

for x in [10,30]:
    nums.remove(x)

print(nums)

### to remove by index range we use del

nums = [10,20,30,40,50,60,70]
del nums[0:3]
print(nums)


## POP - removes value by its index

nums = [10,20,30,40]
nums.pop(2)
print(nums)

nums = [10,20,30]
x = nums.pop()    ## no index is given last item is removed
print(nums)  
print(x) 