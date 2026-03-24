def find_min_max(arr):

    minimum = min(arr)
    maximum = max(arr)

    return minimum, maximum

nums = [3,7,1,9,5]

mn, mx = find_min_max(nums)

print(mn)
print(mx)