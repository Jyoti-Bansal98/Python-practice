## for loop
for i in range(1,4,2):
    print(i)

## reverse loop
n = int(input("n:"))
for i in range(n-1,-1,-2):
    print(i)

## full traversal
arr = [2,5,3,32,3]
for i in range(len(arr)):    # used when one wants to control index
    print(arr[i])           

## direct access -> jab sirf values chaiye control nhi
for i in arr:
    print(i)


## partial loop
arr = ['apple','banana','mango']
for i in range(1, len(arr)):    # used: jab previous element compare karna ho
    print(arr[i])


## reverse loop
for i in range(len(arr)-1, -1, -1):
    print(arr[i])


## nested loop
n = 4
for i in range(n):
    for j in range(n):     ## used for pairs and combinations
        if i>j:
            print(i,j)