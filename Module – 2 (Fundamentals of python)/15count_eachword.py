#Write a Python program to count the occurrences of each word in given sentecne.

s = "Python is the best Programming. Python is high-level programming language."

s = s.split()
#print(s)
#print(len(s))
i=0
count = 0
while i<len(s):
    count = 0
    for j in s:
        if s[i]==j:
            count = count + 1
    print(s[i],":",count)
    i = i+1
