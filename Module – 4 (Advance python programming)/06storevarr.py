#Write a Python program to read a file line by line store it into a variable.

file=open("file.txt","r")
line=file.readlines()

print(line)
