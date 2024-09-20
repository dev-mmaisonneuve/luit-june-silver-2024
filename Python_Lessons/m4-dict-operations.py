grades = {}
grades['John'] = 'A'
grades['Anne'] = 'B'
print(grades)

grades['Anne'] = 'A'
print(grades)

print(len(grades))

del grades ['John']
print(grades)

grades = {}
grades['John'] = 'A-'
grades['Anne'] = 'B'

for el in grades:
    print(el)

for el in grades.keys():
    print(el)

for el in grades.values():
    print(el)

for person, grade in grades.items():
    print(person, 'got', grade)
