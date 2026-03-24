s = input(str())
freq = {}
first_duplicate = None

for ch in s:
    if ch in freq:
        first_duplicate = ch
        break
    freq[ch] =  1

print(first_duplicate)

'''Explanation:
Loop through string, if char already in dict → duplicate exists
Otherwise, add to dict

Time Complexity: O(n)
Space Complexity: O(k)

Pattern:
HashSet / dictionary pattern → fast lookup O(1)'''