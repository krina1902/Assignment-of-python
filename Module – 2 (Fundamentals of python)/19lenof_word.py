#Write a Python function that takes a list of words and returns the length of the longest one.

l = input("Enter few words:")

l1 = l.split()
print(l1)

maxl=0
for i in l1:
   if len(i)>maxl:
    maxl = len(i)
print(maxl)
