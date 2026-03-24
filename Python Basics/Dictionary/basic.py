student = {
    "name": "Joyi",
    "age": 20,
    "city": "Delhi"
}
## Accessing Values   Time complexity- O(1)
print(student['name'])

print(student.get('name')) 
print(student.get('degree', 'no information'))
'''this is better way to access value as it won't give error if key doesn't exist'''


## Adding / Updating
'''Time Complexity: O(1)
Space Complexity: O(1) (only if adding new key, extra memory used)'''

student["age"] = 21      ## age key already exist so age update ho jayegi
student["college"] = "DCRUST"
print(student)


## deleting      Time Complexity: O(1)
del student["college"]
student.pop('marks', 'none')
print(student)


## Looping through dictionary
# a) loop over keys
for key in student:               #  time complexity - O(n),  space complexity - O(1)
    print(key,student[key])       #  Insight: Default iteration gives keys.

# b) Loop using .keys() (explicit)
for key in student.keys():        # complexity same as above
    print(key, student[key])      # useful when u want clarity in code

# c) loop over values
for value in student.values():    # complexity same as above
    print(value)                  # when u don't care about key

# d) Loop over key-value pairs 
for key,value in student.items(): # Output same as keys loop, but cleaner.,  time complexity- O(n)
    print(key, value)             # Use: Most Pythonic and used in interviews.
