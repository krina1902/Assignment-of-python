#Write a Python program to get the Factorial number of given number.

n = int(input("Enter n:"))
fact = 1

if n<0:
    print("factorial is not exists for negative number")
elif n == 0:
    print("the factorial of 0 is 1")
for i in range(1,n+1):
    fact = fact*i
print(fact)
