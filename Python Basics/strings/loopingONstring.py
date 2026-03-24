s = "Joyi"

for ch in s:
    print(ch)

for i in range(len(s)):
    print(i, s[i])    ## s[i] accesses character using index.

s = 'joyi'
i = 0
while i < len(s):    ## important for interview
    print(s[i])
    i += 1

for ch in s[::-1]:
    print(ch)

print(s[::-1])

for i in range(len(s)-1, -1, -1):    ## range(start, stop, step)
    print('ans',s[i])   

s = "Joyi"

for index, ch in enumerate(s):    ## interview friendly
    print(index, ch)

## Loop and Build New String
s = "joyi"
new_s = ""

for ch in s:
    new_s += ch.upper()
print(s)
print(new_s)
