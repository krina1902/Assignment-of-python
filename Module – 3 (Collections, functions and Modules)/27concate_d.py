 #Write a Python script to concatenate following dictionaries to create a new one.

d1={"k":1,"r":2}
d2={"i":3,"n":4}
d3={"a":5}
d4={}

for i in (d1,d2,d3):
    d4.update(i)

print(d4)
