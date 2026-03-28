nums = list(map(int,input().split()))

sq_list = [x*x for x in nums if x%2 == 0]
print(sq_list)

even_list = ['even' if x%2 == 0 else 'odd' for x in nums]
print(even_list)

text = str(input())
upper = [ch.upper() for ch in text]
print(upper)

