def fib(n):
    a = 0
    b = 1

    if n < 0:
        print("Oops, wrong value entered!")
    
    elif n == 1:
        print(a)
    
    else:
        print(a)
        print(b)
        # run loop till range n, starts at 2 since a,b (0,1) are already defined 
        for i in range(2, n):
            c = a + b
            # update after addition
            a = b
            b = c
            print(c)

fib(10)