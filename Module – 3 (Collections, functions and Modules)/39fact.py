#Write a Python function to calculate the factorial of a number (a nonnegative integer)

def factorial(n):
    fact=1
    for i in range(2,n+1):
        fact=fact*i
    print(fact)
    if (n==1)or (n==0):
        return 1
factorial(4)
factorial(1)
factorial(0)
factorial(7)
