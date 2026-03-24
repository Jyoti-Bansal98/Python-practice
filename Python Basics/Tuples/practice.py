nums = (10, 20, 30, 40)
print(nums[0])
print(nums[-1])
print(nums[0:3])

## unpacking
person = ("Joyi", 20, "India")
name, age, country = person
print(name)
print(age)
print(country)


## convert tuples into list

nums = [1,2,3,4]
list = list[nums]
list = nums.append(10)
nums = tuple(nums)
print(nums)

'''Time Complexity   O(n)
Kyuki tuple ke har element ko copy karna padta hai list me.
Space Complexity  O(n)
New list create ho rahi hai.'''

'''Returning Multiple Values from Function (Using Tuple)
Python me jab function multiple values return karta hai, actually tuple return hota hai.'''

def get_values():
    return 10, 20

result = get_values()
print(result)
print(type(result))


