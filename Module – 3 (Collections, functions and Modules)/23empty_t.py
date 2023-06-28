#Write a Python program to remove an empty tuple(s) from a list of tuples.

l=[(),(1,2,3),(""),("a","b","c"),(23,24,25),(),("...")]

for i in l:
     if len(i)==0:
         l.remove(i)
print(l)
