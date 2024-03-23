# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610
# 
def fib(n):
    
    a = 0
    b = 1
    
    if n < 0:
        print(f"Wrong input: {n}")

    elif n == 1:
        print(a)    
    # print(b)
    else: 
        print(a)
        print(b)
        # Use loops to loop through the range
        for i in range(2,n):
            c = a + b
            # Sway numbers after sum of prev values is done
            a = b
            b = c
            print(c)

fib(17)