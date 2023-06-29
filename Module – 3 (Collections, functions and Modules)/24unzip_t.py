#Write a Python program to unzip a list of tuples into individual lists

l=[("k",1),("r",2),("i",3),("n",4),("a",5)]

print(*l)
print(list(zip(*l)))
