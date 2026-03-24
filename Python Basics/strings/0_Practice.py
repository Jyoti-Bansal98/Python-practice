text = "JoyiLearning"

print(text[0])
print(text[-1])
print(text.find('L'))
print(text[4:])
print(text[::-1])

text = "  hello Python World  "

print(text.strip())
print(text.upper())
print(text.replace('Python','AI'))
print(text.count('o'))

text = 'madam'

if text == text[::-1]:
    print('Palindrome')
else:
    print('Not Palinndrome')

count = 0
for ch in text:
    if ch in 'aeiou':
        count += 1

print(count)

text = 'banana'
freq = {}

for ch in text:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1
        
print(freq)