#Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string. 

a = "Tops Technology"
b= "Good habit"

c = b[:2]+a[2:]
d = a[:2]+b[2:]

print("After swap the first two characters:",c,d)

