# Write a Python program to count the number of characters (character frequency) in a string

s = input("Enter String:")
n = {}
for i in s:
    if i in n:
        n[i]+= 1
    else:
        n[i]=1
print(n)
