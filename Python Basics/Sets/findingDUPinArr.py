nums = [1,2,3,2]

seen = set()

for num in nums:
    if num in seen:
        print('Duplicates:',num)

    seen.add(num)

'''Time complexity: O(n)'''

'''Pattern:
1️⃣ create empty set
2️⃣ loop through array
3️⃣ check if element already seen
4️⃣ if yes → duplicate
5️⃣ else → add to set'''

## Loop over set
for num in nums:
    print(num)