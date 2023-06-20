#Write python program that swap two number with temp variable and without temp variable.

#without temp variable
'''
a = int(input("enter a without swap:"))
b = int(input("enter b without swap:"))
a = a+b
b = a-b
a = a-b
print("After swap a is:",a)
print("After swap b is:",b)
'''
#with temp variable
a = int(input("enter a without swap:"))
b = int(input("enter b without swap:"))

temp = a
a = b
b = temp
print("After swap a is:",a)
print("After swap b is:",b)
