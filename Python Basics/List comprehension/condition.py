nums = list(map(int,input().split()))
condition = ['even' if n%2 == 0 else 'odd' for n in nums]
print(condition)