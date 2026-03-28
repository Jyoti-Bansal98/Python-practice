students = { ('joyi',21), ('lucky',19), ('arjun',7)}
sorted_students = sorted(students, key = lambda x:x[1])
print(sorted_students)

pairs = [(1, 3), (2, 1), (4, 2)]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print(sorted_pairs)

# x[1] → second element ke basis par sort


students = [("Joyi", 20), ("Aman", 24), ("Riya", 22)]
sorting_students = sorted(students, key=lambda x: x[0])
print(sorting_students)
sorting_students  = sorted(students, key = lambda x: x[1])
print(sorting_students)
