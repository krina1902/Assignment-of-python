#Write a Python function that takes two lists and returns true if they have at least one common member.

def common_member(l1,l2):
    for i in l1:
        for j in l2:
            if i==j:
                return True
    else:
        print("They have no commom member.")
            
l1=[1,2,3,4,5]
l2=[5,6,7,8,9]
l3=[1,2,3,4]
print(common_member(l1,l3))
print(common_member(l3,l2))
