#Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string

s = "your book is not so poor really."
no = s.find("not")
poor = s.find("poor")

if no<poor and no != -1:
    print(s[:no]+"good"+s[poor+4:])
    

