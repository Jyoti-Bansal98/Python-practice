def sum(nums):
    total = 0

    for num in nums:
        total += num
    return total

nums = list(map(int,input().split()))
print(sum(nums))

'''Time complexity = O(n)
space complexity = O(1)'''
