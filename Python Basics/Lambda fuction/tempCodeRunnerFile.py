

students = [("Joyi", 20), ("Aman", 24), ("Riya", 22)]
sorting_students = sorted(students, key=lambda x: x[0])
print(sorting_students)
sorting_students  = sorted(students, key = lambda x: x[1])
print(sorting_students)