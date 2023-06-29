#Write a Python program to convert a list of tuples into a dictionary.

l=[("x",1),("x",2),("y",4),("z",4),("z",6),("y",7),("y",8),("x",5),("y",6),("x",4)]
d={}

for a,b in l:
    d.setdefault(a,[]).append(b)

print(d)
