#Write a Python program to get the Fibonacci series of given range. 

a,b=0,1
n = int(input("Enter n:"))

print(a,end=" ")
while b<n:
    print(b,end=" ")
    a,b=b,a+b
