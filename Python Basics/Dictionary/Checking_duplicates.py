s = 'programming'
freq = {}
has_duplicates = False

for ch in s:
    if ch in freq:
        has_duplicates = True
        break
    freq[ch] = 1

print('Does',s, 'has duplicates:', has_duplicates)

'''Explanation:
Loop through string, if char already in dict → duplicate exists
Otherwise, add to dict   

mtlb in short s me jitne bhi ch hai vo freq me chale jate hai and its
like ki - if ch in freq mtlb agar ch phelee se freq me hai toh true return krdo or break krdo 
code but agar ch freq me nhi hai toh freq me uss ch ki freqency/count = 1 krdo

Time Complexity: O(n)
Space Complexity: O(k)

Pattern:
HashSet / dictionary pattern → fast lookup O(1)'''

