#Write a Python program to read an entire text file.

file=open("file.txt","w")
file.write("Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation via the off-side rule")
file.close()

file=open("file.txt","r")
print(file.read())
file.close()
