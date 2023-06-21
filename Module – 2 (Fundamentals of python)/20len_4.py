#Write a Python function to reverses a string if its length is a multiple of 4.

s = input("Enter String:")

if len(s)%4 == 0:
    print(s[::-1])
else:
    print("The length is not multiple of 4.")

