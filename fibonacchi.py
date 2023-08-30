"""






# 5! -> 5*4*3*2*1
# 4! -> 4*3*2*1
# 3! -> 3*2*1
# 2! -> 2*1

user_input = int(input("Enter the number for series: "))
n = int(input("Enter the size of list : "))
print(f"You entered {user_input}.")
eg_list = []

for i in range(1, user_input):
    eg_list.append(i)
print(type(eg_list[::-1]))
print(eg_list[::-1])

def multiply_list(my_list):
    result = 1
    for i in my_list:    
        result = result * i
    return result



print(f"Sum of fibonnaci series is : {multiply_list(eg_list)}")
#output = eg_list[::-1]
#print(output)



# Garbage
"""

# Sum of fib
def Fib(n):
    if n < 0:
        print(f"Wrong input: {n}")

    elif n==0:
        return 0
    
    elif n==1 or n==2:
        return 1

    else:
        return Fib(n-1) + Fib(n-2)

print(f"Total of the number is: {Fib(10)}")

# 2 : Print Fib

def fibb(n):

    a = 0
    b = 1

    if n < 0:
        print(f"Wrong input: {n}")

    elif n==0:
        return 0
    
    else:
        print(a)
        print(b)

        for i in range(2,n):
            c = a + b
            # update values 
            a = b 
            b = c

            print(c)

fibb(5)




