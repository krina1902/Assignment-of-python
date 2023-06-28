#Write a Python program to check whether a list contains a sub list

l=[1,2,3,4,5,6,7,8,9]
sublist=[6,7,8,9,5]

count=0
for i in sublist:
    if i in l:
        count=count+1
print(count)
if(count==len(sublist)):
    print("The sublist is present in original list.")
else:
    print("The sublist is not present in original list.")
