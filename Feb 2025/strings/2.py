a = '   Hello Joyi, How are you. I love you.   '
print(a.lower())
print(a.upper())   # Case-insensitive comparison karna ho
print(a.count('l'))
print(a.find('love'))
print(a.istitle())
### original string kabhi change nhi hoti string immutablle hoti hai.
print(a.strip())
print(a.rstrip())   # right side se remove
print(a.lstrip())   # left side se remove
print(a.replace('love','hate'))
print(a.split())     ## space ke bases par split karta hai, string -> list convert hoti hai.
print(a.split(','))   ## custom kr sakte hai split ko

name = "joyi"
print(name.upper() == "JOYI")  # True
print(name)

fruits = ['apple', 'banana', 'mango']
print(" ".join(fruits))    ## convert list -> string.
print(", ".join(fruits))    ## Join hamesha string pe call hota hai, list pe nahi.

text = "   Python is FUN and fun   "
print(text.split(), text.count('FUN'), text.lower())
print(len(a))
print(text[:14])
print(text[:-7])
print(text[::2])
print(text[::-1])

