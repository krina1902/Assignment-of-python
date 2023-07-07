#Write a Python program to read first n lines of a file.




n = int(input("Enter Lines To Read : "))
f = open("file.txt","r")
linelist=f.readlines()
for i in (linelist[:n]):
	print(i,end="")



