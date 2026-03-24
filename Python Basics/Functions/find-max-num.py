def max_num(nums):
    max_val = nums[0]

    for num in nums[1:]:
        if num > max_val:
            max_val = num
    return max_val
        
# nums = input()
nums = list(map(int,input().split()))
print(max_num(nums))

'''time complexity = O(n)
space complexity = O(1)'''