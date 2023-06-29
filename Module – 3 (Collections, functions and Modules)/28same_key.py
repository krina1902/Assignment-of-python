#Write a Python script to check if a given key already exists in a dictionary.

d={1:10,2:20,3:30,4:40,5:50}

def present(i):
    if i in d:
        print("Key is present in dictionary")
    else:
        print("Key is not present in dictionary")

present(2)
present(8)
