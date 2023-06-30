#Write a Python function to check whether a number is in a given range

def range1(n):
    if n in range(1,1000):
        print(n,"number is in a given range...")
    else:
        print(n,"number is not in a given range...")

range1(900)
range1(0)
