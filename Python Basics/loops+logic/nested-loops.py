'''Loop inside a loop
i → outer loop (rows)
j → inner loop (columns)'''

for i in range(3):
    for j in range(3):
        print(i,j)

'''outer loop → 3 times
inner loop → har baar 3 times
total → 3 x 3 = 9 iterations'''

## pattern recogination: nested loop = combinations / pairs
nums = [1,2,3]
for i in range(len(nums)):
    for j in range(len(nums)):
        print(nums[i], nums[j])

# square pattern
for i in range(3):
    for j in range(3):
        print('*',end = ' ')
    print()

# triangle pattern
for i in range(1,6):
    for j in range(i):
        print('*',end = ' ')
    print()


# Avoid duplicated
nums = [1,2,3]
for i in range(len(nums)):
    for j in range(i+1,len(nums)):  # i+1 duplicate pairs na aaye (1,2) aaye but (2,1) na aaye
        print(nums[i], nums[j])


