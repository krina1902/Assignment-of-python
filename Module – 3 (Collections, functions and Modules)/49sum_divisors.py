#Write a Python program to returns sum of all divisors of a number

n=int(input("Enter number:"))

div=[]

for i in range(1,n):
    if n%i==0:
        div.append(i)
print("Sum of all divisors of a number is ",sum(div))
      
