#Write a python program to find the longest words.

file = open("file.txt","r")

word=file.read().split()
maxl=len(max(word,key=len))
for i in word:
    if len(i)==maxl:
        print(i)
