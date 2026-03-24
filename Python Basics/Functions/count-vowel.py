def count_vowels(word):
    count = 0

    for ch in word:
        if ch in 'aeiouAEIOU':
            count+= 1
    return count

word = input()
print(count_vowels(word))

'''Time complexity = O(n)
space complexity = O(1)'''
