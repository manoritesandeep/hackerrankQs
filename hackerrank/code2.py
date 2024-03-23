"""
Task
The provided code stub reads two integers, a and b, from STDIN.

Add logic to print two lines. The first line should contain the result of integer division,
// . The second line should contain the result of float division

No rounding or formatting is necessary.

Example:
a = 3
b = 5

The result of the integer division 3//5=0

The result of the float division is 3/5=0.6

Print:

0
0.6

"""

if __name__ == "__main__":
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))

    print(a//b)
    print(a/b)
