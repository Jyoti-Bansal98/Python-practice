## 3) Character count
text = 'programming'
freq = {}

for ch in text:
    freq[ch] = freq.get(ch,0) + 1

print(freq)


## 4) Find most frequent element 
nums = [12,12,13,443,422,14,12,13,14]
freq =  {}

for num in nums:
    freq[num] = freq.get(num,0) + 1

print(freq)

max_count = 0
result = None

for num in freq:
    if freq[num] > max_count:
        max_count = freq[num]
        result = num

print(result)

'''Time Complexity:  O(n) → one pass for freq + one pass for dict
Space Complexity:  O(k) → k = unique elements'''

nums = [1, 3, 2, 3, 4, 3, 2]

freq = {}

for num in nums:
    freq[num] = freq.get(num, 0) + 1

print(max(freq, key=freq.get))

