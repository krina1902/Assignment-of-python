#Write a Python program to check multiple keys exists in a dictionary

d={"A":1,"B":2,"C":3,"D":4,"E":5}

print(d.keys() >= {"A","B"})
print(d.keys() >= {"A","1"})
print(d.keys() >= {"2","B"})
print(d.keys() >= {"E","D"})
