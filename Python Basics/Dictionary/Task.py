## 1) basic
student = {
    "name": "Joyi",
    "age": 20
}

print(student['name'])
student['City'] = 'Delhi'
student['age'] = 21

print(student)


## 2) Frequency counter
nums = [1,2,2,3,3,3,4]
freq = {}

for num in nums:
        freq[num] = freq.get(num,0) + 1

print(freq)

