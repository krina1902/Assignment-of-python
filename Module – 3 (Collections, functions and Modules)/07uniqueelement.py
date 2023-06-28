#Write a Python function that takes a list and returns a new list with unique elements of the first list.

def clist(l):
    unique_list=[]
    for i in l:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list


l1=[1,1,2,2,3,4,5,6,7,7,8,9]
print("The first unique_list is:",clist(l1))
