#Write a Python program to write a list to a file. 

items = ['Mango', 'Orange', 'Apple', 'Lemon']
file = open('file1.txt','w')
for i in items:
	file.write(i +"\n")
file.close()
