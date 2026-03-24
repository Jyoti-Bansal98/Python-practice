## 1️⃣ get()
student = {"name": "Jyoti", "age": 21}

# Direct access (unsafe)
''' print(student["marks"])   # KeyError if key doesn't exist'''

# Safe access
print(student.get("marks"))        # None
print(student.get("marks", 0))     # 0 (default value)

'''Time Complexity: O(1)
Space Complexity: O(1)'''


## 2️⃣ key()   Purpose: get all keys of the dictionary
student = {"name": "Jyoti", "age": 21}

print(student.keys())

for key in student.keys():    # can iterate over keys
    print(key, student[key])

'''Time Complexity: O(n) to iterate
Space Complexity: O(1) (returns view, not copy)'''


## 3️⃣ values()   Purpose: get all values of the dictionary
print(student.values())

for value in student.values():   # can iterate over values
    print(value)
'''Time Complexity: O(n) to iterate
Space Complexity: O(1) (view, no extra copy)'''


## 4️⃣ items()   Purpose: Get key-value pairs as tuples.
print(student.items())

for key, value in student.items():   # looping over items (pythonic way)
    print(key, value)
'''Time Complexity: O(n)
Space Complexity: O(1) (view, not copy)

Use case: Most common pattern for iterating dictionaries in DSA.'''


## 5️⃣ pop()    Purpose: Remove a key and return its value
marks = {"math": 95, "science": 90}

val = marks.pop("math")
print(val)     # 95
print(marks)   # {'science': 90}

# Using default to avoid KeyError
marks.pop("english", 0)   # returns 0, doesn't error

'''Time Complexity: O(1) average
Space Complexity: O(1)

Use case: Remove keys safely while fetching value (like removing processed items in DSA problems).'''


## 6️⃣ update()    Purpose: Add or update multiple key-value pairs at once.
student = {"name": "Jyoti", "age": 21}

# Update existing key and add new key
student.update({"age": 22, "marks": 95})
print(student)
'''Time Complexity: O(len(dict2)) → number of keys being updated
Space Complexity: O(1) (in-place update)

Use case: Merge dictionaries or bulk update values efficiently.'''


