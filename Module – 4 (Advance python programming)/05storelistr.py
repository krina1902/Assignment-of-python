#Write a Python program to read a file line by line and store it into a list

file=open("file.txt","r")
line=file.readlines()
print(line)

line=[i.strip() for i in line]
print(line)#remove \n
