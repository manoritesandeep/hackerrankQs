"""
Task:

The provided code stub reads and integer, n, from STDIN. 
For all non-negative integers i < n, print i^2. 
"""

if __name__ == '__main__':
    n = int(input("Enter a number: "))

    for x in range(n):
        print(x ** 2)


##### OR #####

if __name__ == "__main__":
    n = int(input("Enter a number: "))

    print([x**2 for x in range(n)])