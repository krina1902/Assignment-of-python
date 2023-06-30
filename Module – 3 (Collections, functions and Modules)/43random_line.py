#Write a Python program to read a random line from a file.

import random
file=open("44myFile.txt","w")
file.write("welocome to page....")
file.write("random line from file....")
file.close()

print(random.choice(open("44myFile.txt","r").readline().split()))
