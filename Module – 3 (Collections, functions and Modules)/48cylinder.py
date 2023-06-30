#Write a Python program to calculate surface volume and area of a cylinder

r=float(input("Enter radius of cylinder:"))
h=float(input("Enter height of cylinder:"))
pi=22/7

volume=2*pi*r*r*h
area=(2*pi*r*r)+(2*pi*r*h)

print("Surface volume of a cylinder is:",volume)
print("Surface area of a cylinder is:",area)
