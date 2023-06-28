#Write a Python program to get unique values from a list

l=[1,2,3,44,44,5,6,56,65,56,67,67,78,78,2]
ul=[]
for i in l:
    if i not in ul:
        ul.append(i)

for i in ul:
    print(i , end=" ")
