nums = [1,2,3,4,2,5,3]
dup = []

for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] == nums[j] and nums[i] not in dup:
            dup.append(nums[i])

print(dup)

'''Time Complexity: O(n²), Because of nested loops.
Space Complexity: O(k),  k = number of duplicates.'''


### using Set better solution, idea: it keeps track of seen elements

nums = [12, 24,33,12,45,33,12,21,12]

seen = set()
duplicates = set()

for num in nums:
    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)

print(duplicates)
print(seen)
''' Time Complexity = O(n), Each element checked once.
Space Complexity = O(n),  Because of set.'''


## using count not efficient as count itself time complexity is O(n)

nums = [1,2,3,4,2,5,3]
duplicates = []

for num in nums:
    if nums.count(num) > 1 and num not in duplicates:
        duplicates.append(num)

print(duplicates)


nums = [1,2,3,4,2,5,3]

duplicates = list(set([x for x in nums if nums.count(x) > 1]))
print(duplicates)

