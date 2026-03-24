s = "joyi"
count = 0

for ch in s:
    if ch in "aeiou":
        count += 1

print(count)

message = 'I Love Coding'
count = 0

for ch in message:
    if ch in 'aeiouAEIOU':
        count += 1

print(count)

## Frequency of character in string

a = 'banana'
freq = {}

for ch in a:
    freq[ch] = freq.get(ch, 0) + 1

print(freq)

## another method
for ch in a:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print(freq)

## to find first non repetive character
s = "swiss"
freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

for ch in s:
    if freq[ch] == 1:
        print(ch)
        break
