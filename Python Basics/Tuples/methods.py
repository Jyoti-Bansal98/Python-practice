## count method
numbers = (10, 20, 30, 20, 40)
print(numbers.count(20))

letters = ('a', 'b', 'a', 'c', 'a')

print(letters.count('a'))     

'''time complexity O(n)
yunki tuple ko poora traverse karna padta hai.
Space Complexity  O(1)
Extra memory use nahi hoti.'''

numbers = (10, 20, 30, 20, 40)

print(numbers.index(20))     ## first occurence return krta hai

'''Time Complexity  O(n)
Worst case me end tak search karega.
Space Complexity   O(1)'''

'''Tuple mostly use hota hai:

multiple values return karne ke liye
dictionary keys'''

# example:
def get_user():
    return ("Joyi", 20)

name, age = get_user()
print(name,age)

