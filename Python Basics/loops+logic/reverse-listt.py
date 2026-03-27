# nums = [1,2,3,4]
def reverse_list(nums):
    new_nums = []

    for i in range(len(nums)-1,-1,-1):
        new_nums.append(nums[i])
    return new_nums

nums = list(map(int,input().split()))
print(nums)
print(reverse_list(nums))

