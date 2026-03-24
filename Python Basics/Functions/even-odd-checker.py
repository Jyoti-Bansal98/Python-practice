def checker(num):
    remainder = num%2

    if remainder == 0:
        return 'even'
    else:
        return 'odd'
    
num = int(input('num:'))
print(checker(num))

'''time complexity: O(1)
space complexity: O(1)'''