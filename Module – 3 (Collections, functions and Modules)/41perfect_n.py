#Write a Python function to check whether a number is perfect or not.

def perfectn(n):
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum=sum+i
    return sum==n

print(perfectn(6))
print(perfectn(9))
print(perfectn(28))
print(perfectn(496))
