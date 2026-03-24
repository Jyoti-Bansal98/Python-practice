def reverse_string(string):
    new_string = ""

    for i in range(len(string)-1,-1,-1):
        new_string += "".join(string[i])
    return new_string

string = str(input())
print(reverse_string(string))

'''Time complexity: O(n)
space complexity: O(n)'''
