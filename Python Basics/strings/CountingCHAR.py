s = 'banana'
freq = {}

for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print(freq)

from collections import Counter

s = "banana"
freq = Counter(s)
print(freq)
