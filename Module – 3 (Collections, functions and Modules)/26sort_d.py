#Write a Python script to sort (ascending and descending) a dictionary by value

d = {'c': 3,
           'a': 1,
           'd': 4,
           'b': 2}
 
s = sorted([(value, key)
 for (key, value) in d.items()])
 

print("Sorted dictionary is :")
print(s)
