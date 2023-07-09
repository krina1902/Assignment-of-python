#Write python program that user to enter only odd numbers, else will raise an exception.

try:
    n=int(input("Enter value of n:"))
    assert n%2==0
except:
    print("Exception caught")
