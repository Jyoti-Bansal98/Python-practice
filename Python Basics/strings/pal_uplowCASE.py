s = "A man a plan a canal Panama"

s = s.lower()
s = s.replace(" ", "")

if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")


## For two pointer

s = "A man a plan a canal Panama"
s= "".join(ch.lower() for ch in s if ch.isalnum())

left = 0
right = len(s) - 1

while left < right:
    if s[left] != s[right]:
        print('not palindrome')
        break
    left += 1
    right -= 1
else:
    print('palindrome')
