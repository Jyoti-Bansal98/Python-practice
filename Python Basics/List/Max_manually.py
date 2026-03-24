numbers = [5,2,9,1,7,34]

max = numbers[0]

for num in numbers:
    if num > max:
        max = num
print(max)


## Interviewer may ask:  What if list is empty?

nums = [5, 2, 9, 1, 7]

if len(nums) == 0:
    print("List is empty")
else:
    max_num = nums[0]

    for num in nums:
        if num > max_num:
            max_num = num

    print(max_num)


## skipping first element because first element is already stored

nums = [5, 56,99,234, 2,54,64]

max_num = nums[0]
min_num = nums[0]

for num in nums[1:]:
    if num > max_num:
        max_num = num
    elif num < min_num:
        min_num = num 

print(max_num)
print(min_num)
''' time complexity is O(n), space is O(1), if we use two loops than time complexity will be 
O(2n) so inside a single loop is a better solution.'''

