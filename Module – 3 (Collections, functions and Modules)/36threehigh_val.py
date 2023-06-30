#Write a Python program to find the highest 3 values in a dictionary

from heapq import nlargest

d={"a":54,"b":78,"c":76,"d":98,"e":87}

threeh=nlargest(3,d,key=d.get)
print(threeh)

for i in threeh:
    print(i ,":" , d[i])
