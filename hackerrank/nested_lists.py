"""
Given the names and grades for each student in a class of N students, 
store them in a nested list and print the name(s) of any student(s) 
having the second lowest grade. 

Note: If there are multiple students with the second lowest grade, 
order their names alphabetically and print each name on a new line.
"""
students = [['Harry', 37.21], 
            ['Berry', 37.21], 
            ['Tina', 37.2], 
            ['Akriti', 41], 
            ['Harsh', 39]]

# print(students[0][1]) #37.21

min_grade = min([g[1] for g in students])
print(f"Min grade is: {min_grade}")

second_min = None
names = []
for name, grade in students:
    print(grade)
    # print(name,grade)
    if grade == min_grade:
        pass
    elif second_min == None:
        second_min = grade
        print(f"Elif1: {second_min}")   # 37.21
    elif grade <= second_min:
        names.append(name)
        print(f"Elif2: {second_min}")
print(names)
