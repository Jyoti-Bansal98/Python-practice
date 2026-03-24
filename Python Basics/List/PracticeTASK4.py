## Remove Duplicates

nums = [1,2,2,3,4,4,5]

seen = set()
duplicates = set()

for num in nums:
    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)

print(duplicates)