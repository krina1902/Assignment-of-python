#Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add en'ly' instead if the string length of the given string is less than 3, leave it unchanged.

s = input("Enter string:")

if len(s)<3:
    print(s)
elif s[-3:] == "ing":
    print(s + "ly")
else:
    print(s + "ing")
