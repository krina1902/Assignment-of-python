#Write a Python program to print all unique values in a dictionary.
students = [{'Smith':58, 'John':54, 'Priska':53, 'Abhi':54}]

unique=set(a for i in students for a in i.values())

print("The unique values are:",unique)
