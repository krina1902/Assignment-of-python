#Write a Python program to count the frequency of words in a file.

from collections import Counter

file=open("file.txt","r")
word=file.read().split()
print(Counter(word))
