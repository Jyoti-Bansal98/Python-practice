def count_lines(filename):
    with open('test.txt', "r") as file:
        count = 0
        for line in file:
            count += 1
    return count

print(count_lines('test.txt'))

