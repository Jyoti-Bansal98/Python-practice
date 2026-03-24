nums = {1,2,3}
print(nums)
nums = set([1,2,3])
print(nums)


## add method
'''Time complexity: O(1)
space complexity: O(1)
because hash table use hota hai'''

s = {1,2,3}
s.add(4)
print(s)

s = {1,2,3}   ## duplicate add nhi hota
s.add(2)
print(s)


## remove method
s = {1,2,3,4}
s.remove(3)
print(s)
# s.remove(10)   give key error if element is not present.


## discard method removes without error
s = {1,2,3}
s.discard(5)
print(s)
# discard is safer than remove


## pop method:  Set se random element remove karta hai.
s = {1,2,3}   # because sets are unordered
s.pop()
print(s)


## union method: combines two sets
''' complexity: O(n + m)'''
a = {1,2,3}
b = {3,4,5}

c = a.union(b)   # duplicates automatically remove ho jata hai
print(c)
print(a|b)


## intersection: Common elements return karta hai.
a = {1,2,3}
b = {2,3,4}

print(a.intersection(b))
print(a&b)


## difference method:  Set1 me jo elements hai but set2 me nahi.
a = {1,2,3}
b = {2,3,4}

print(a.difference(b))
print(a-b)

