#Write a Python program to read last n lines of a file. 

n=int(input("Enter no of lines:"))
f=open("file.txt","r")
linelist=f.readlines()
for i in linelist[-n:]:
    print(i,end="")
