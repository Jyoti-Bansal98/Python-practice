nums  = list(map(int,input().split()))
sq = {num: num*num for num in nums}
print(sq)

even_sq = {num: num*num for num in nums if num%2 == 0}
print(even_sq)

word = str(input())
ch_count = {ch: word.count(ch) for ch in word}  #this is not efficient, Better approach (freq dictionary loop wala)
print(ch_count)  

