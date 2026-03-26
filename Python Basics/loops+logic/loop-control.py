## break
def find_first_even(nums):

    for num in nums:
        if num%2 == 0:
            result  = num
            break
    return result
        
nums = list(map(int,input().split()))
print(find_first_even(nums))
'''return → function hi end
break → sirf loop end'''

## continue
def sum_even(nums):
    total = 0

    for num in nums:
        if num%2 != 0:
            continue
        total += num
    return total

nums = list(map(int, input().split()))
print(sum_even(nums))


## pass
def check(nums):
    for num in nums:
        if num < 0:
            pass   # abhi kuch nahi karna
        else:
            return num
        
nums = list(map(int,input().split()))
print(check(nums))


for i in range(5):
    if i == 2:
        continue
    print(i)