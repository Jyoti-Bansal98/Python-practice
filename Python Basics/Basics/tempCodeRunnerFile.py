nums = [1, 2, 14, 19, 22, 3, 5, 7]

total = 0
maximum = nums[0]
even = 0
for i in nums:
    if i> maximum:
        maximum = i

    if i%2 == 0:
        even = even + 1

    print(i)
    total += i


print(total)