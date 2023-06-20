#Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.

a=int(input("Enter a:"))
b=int(input("Enter b:"))
c=int(input("Enter c:"))
sum=a+b+c
if a==b or b==c or a==c:
    sum=0
    print("sum of three integers when two are equals:",sum)
else:
    sum=a+b+c
    print("sum of three integers:",sum)
