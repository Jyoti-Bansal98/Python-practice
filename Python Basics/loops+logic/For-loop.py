def list(n):
    nums  = []

    for i in range(1,n):
        nums.append(i)
    return nums

n  = int(input())
print(list(n))

## return sum of list
def sum(n):
    total = 0 

    for i in n:
        total += i
    return total

n = list(map(int,input().split()))
print(sum(n))