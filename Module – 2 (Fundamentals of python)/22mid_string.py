#Write a Python function to insert a string in the middle of a string.

string = input("Enter String:")
mids = input("Enter mid string:")

l = len(string)
m = int(l/2)

print(m)
print(string[:m] + mids + string[m:]) 
