def find_max(nums):
    max = nums[0]

    for num in nums:
        if num > max:
            max = num
    return max

nums = list(map(int,input().split()))
print(find_max(nums))

