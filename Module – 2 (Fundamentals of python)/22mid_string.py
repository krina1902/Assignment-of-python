#Write a Python function to insert a string in the middle of a string.

string = input("Enter String:")
mids = input("Enter mid string:")

w=string.split()
m = len(w)
print(m)

s = "".join(w[m:]+mids+w[:m])
print(s)
