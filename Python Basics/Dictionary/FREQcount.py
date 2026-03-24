s = "aaabbc"
freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

print(freq)

'''Time Complexity: O(n) → loop over string
Space Complexity: O(k) → k = number of unique characters
Insight: This pattern is golden for anagrams, counting duplicates, etc.'''

'''This is a frequency counting pattern → used in duplicate check, anagram, 
first non-repeating character, etc.'''