#Write a Python function to get the largest number, smallest num and sum of all from a list.

def Max(l) :
    maxi=l[0]
    for i in l:
        if i>maxi:
            maxi = i
    return maxi



def Mini(l):
    mini=l[0]
    for i in l:
        if i<mini:
            mini = i
    return mini

def sum(l):
    sum=0
    for i in l:
        sum=sum+i
    return sum

l=[1,2,3,40,5,6,45,67,300,98,0,342]
print("Largest number in list:",Max(l))
print("Smallest number in list:",Mini(l))
print("Sum of all numbers in list:",sum(l))
    
