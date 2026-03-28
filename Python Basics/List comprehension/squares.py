num = list(map(int,input().split()))
sq = [n*n for n in num if n%2 == 0]
print(sq)