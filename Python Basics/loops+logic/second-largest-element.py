def second_largest(nums):
    largest = nums[0]
    second = nums[1]

    for num in nums:
        if num > largest:
            second = largest
            largest = num
        elif num > largest and num != largest:
            second = num
    return largest, second

nums = list(map(int,input().split()))
print(second_largest(nums))

'''Time Complexity = O(n)
Space Complexity = O(1) '''