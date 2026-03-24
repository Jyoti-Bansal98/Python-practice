## Index

nums = [10, 20, 30, 40]
print(nums.index(30))

nums = [1,2,3,2,4]
print(nums.index(2))   ## It returns the FIRST occurrence only

nums = [1,2,3]

if 2 in nums:
    print(nums.index(2))


## Count

fruits = ["apple","banana","apple","mango"]
print(fruits.count("apple"))



nums = [1,1,1,2,2,3]

if nums.count(1) > 2:
    print("1 appears many times")
print(nums[:4])

