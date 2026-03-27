n = int(input())
for i in range(1,n+1):
    print(i)

total = 0
for i in range(n):
    total += i
print(total)
    
## count even numbers
count = 0
for i in range(n):
    if i%2 == 0:
        count += 1
print(count)


## star-triangle pattern
for i in range(1,n):
    for j in range(i):
        print('*',end = ' ')
    print()

## mulltiplication table
for i in range(1,11):
    print(n*i)

## break and continue
for i in range(5):
    if i%2== 0:
        continue
    print(i)

for i in range(10):
    if i == 8:
        break
    print(i)

