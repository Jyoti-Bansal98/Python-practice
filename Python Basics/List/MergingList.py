list1 = [1,2,3]
list2 = [4,5,6]

merged = list1 + list2
print(merged)
''' Time Complexity = O(n + m)
n = length of list1
m = length of list2

Space Complexity = O(n + m),,  bcoz a new list is created'''


## using extend
list1 = [10,34,3]
list2 = [4,25,6]

list1.extend(list2)
print(list1)


## using loops
list1 = [1,2,3]
list2 = [4,5,6]

for num in list2:
    list1.append(num)

print(list1)