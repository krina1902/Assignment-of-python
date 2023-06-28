#Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.

l=["abcd","acfca","12321","ab","going","L","KK"]

count=0
for i in l:
    if len(i)>1 and i[0]==i[-1]:
        count=count+1
print("Count the number of string:",count)
