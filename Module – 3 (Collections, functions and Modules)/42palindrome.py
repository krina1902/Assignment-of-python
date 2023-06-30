#Write a Python function that checks whether a passed string is palindrome or not

def palindrome(s):
    if s == s[::-1]:
        print(s,"string is palindrome")
    else:
        print(s,"string is not palindrome")


s1="qbcbq"
palindrome(s1)
s2="krina"
palindrome(s2)
        
    
