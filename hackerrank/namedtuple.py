"""
collections.namedtuple()

Basically, namedtuples are easy to create, lightweight object types.
They turn tuples into convenient containers for simple tasks.
With namedtuples, you don’t have to use integer indices for 
    accessing members of a tuple.

Task:
Dr. John Wesley has a spreadsheet containing a list of student's
IDs, marks, class and name.

Your task is to help Dr. Wesley calculate the average 
    marks of the students.

Average = Sum of all marks / Total Students
    
Note:
1. Columns can be in any order. 
    IDs, marks, class and name can be written in any order
      in the spreadsheet.
2. Column names are ID, MARKS, CLASS and NAME. 
    (The spelling and case type of these names won't change.)
 
"""

from collections import namedtuple
import io
import sys

Point = namedtuple('Point','x,y')
pt1 = Point(1,2)
pt2 = Point(3,4)
print(pt1,pt2)
dot_product = ( pt1.x * pt2.x ) + ( pt1.y * pt2.y )
print(dot_product)

from collections import namedtuple
Car = namedtuple('Car','Price Mileage Colour Class')
xyz = Car(Price = 100000, 
          Mileage = 30, 
          Colour = 'Cyan', 
          Class = 'Y')
print(xyz)
Car(Price=100000, 
    Mileage=30, 
    Colour='Cyan', 
    Class='Y')
print(xyz.Class)

#####################################################
# Namedtuple

sample_input = '''5
ID MARKS NAME CLASS
1 97 Raymond 7
2 50 Adam 6
3 68 Eve 7
4 88 Alice 8
5 92 Bob 7
'''

# Redirect standard input to read from sample_input
sys.stdin = io.StringIO(sample_input)

num_students = int(input())
# num_students = 5

# no need to map, since input is already string.
cols = input().split()
# cols = ["ID", "MARKS", "NAME", "CLASS"]

Student = namedtuple('Student', ' '.join(cols))

# ray = Student(1, 97, 'Raymond', '7')
# print(ray, ray.MARKS)

# The * operator is used to unpack the list of words into separate arguments for the Student constructor.
students = [Student(*input().split()) for _ in range(num_students)]
# print(students)

"""
[Student(ID='1', MARKS='97', NAME='Raymond', CLASS='7'), 
    Student(ID='2', MARKS='50', NAME='Adam', CLASS='6'), 
    Student(ID='3', MARKS='68', NAME='Eve', CLASS='7'), 
    Student(ID='4', MARKS='88', NAME='Alice', CLASS='8'), 
    Student(ID='5', MARKS='92', NAME='Bob', CLASS='7')
]
"""

# Calculate average marks: Average = Sum of all marks / Total Students
total_students = len(students)
marks_obtain = [_.MARKS for _ in students]
total_marks = sum([int(_.MARKS) for _ in students])
print(f"Total students: {total_students}, \
        \nMarks obtain: {marks_obtain}, \
        \nTotal marks: {total_marks}")

avergae_marks = total_marks / total_students
print(f"Average marks: {avergae_marks:.2f}")

## Can you solve this challenge in 4 lines of code or less?
# print("{:.2f}".format(sum([int(student.MARKS) for student in students]) / len(students))




