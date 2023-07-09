#Write a Python program to copy the contents of a file to another file.

f1=open("file.txt","r")
f2=open("file1.txt","a")

for i in f1:
    f2.write(i)

f1.close()
f2.close()
