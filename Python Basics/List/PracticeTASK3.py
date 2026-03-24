## find largest number in list

nums = [10, 20, 30, 40, 50]
max = nums[0]

for num in nums[1:]:
    if num > max:
        max = num

print(max)


## reverse list without using reverse
print(nums[::-1])


## count even nums

nums = [2,4,23,54,64,67]
even = 0
for num in nums:
    if num%2 == 0:
        print(num)

