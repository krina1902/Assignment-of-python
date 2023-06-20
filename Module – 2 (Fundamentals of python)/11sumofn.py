# Write a python program to sum of the first n positive integers.

n=int(input("Enter n:"))
sum=0
for i in range(1,n+1):
    sum=sum+n
    n=n-1
print(sum)
