s = 'madam'

left = 0
right = len(s) - 1

while left < right:
    if s[left] != s[right]:
        print('Non Palindrome')
        break
    left += 1
    right -= 1
else:
   print('Palindrome')

## Why Two Pointer Is Powerful?
## Because: It only checks half string.,
## Time complexity = O( n) 
## Space complexity = O(1)
