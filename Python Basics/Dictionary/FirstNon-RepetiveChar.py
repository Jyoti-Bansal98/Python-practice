s = input(str('s:'))
freq = {}

for ch in s:
    freq[ch] = freq.get(ch,0) + 1

first_unique = None

for ch in s:
    if freq[ch] == 1:
        first_unique = ch
        break

print(first_unique)

'''Time Complexity: O(n)
Space Complexity: O(k)'''