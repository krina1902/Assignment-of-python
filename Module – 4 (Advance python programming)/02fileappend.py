#Write a Python program to append text to a file and display the text.
file=open("file.txt","w")
file.write("Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation via the off-side rule")
file.close()

file=open("file.txt","a")
file.write("\nWithout a doubt one of the most important poems of the 20th century. \n“It has never lost its glamour,” Paul Muldoon observed. \n“It has never failed to be equal to both the fracture of its own era and what,\n alas, turned out to be the even greater fracture of the ongoing 20th century and now,\n it seems, the 21st century.” See also: “The Love Song of J. Alfred Prufrock.Robert Frost, \n“The Road Not Taken”Otherwise known as “the most misread poem in America.” \nSee also: “Stopping by Woods on a Snowy Evening.” And “Birches.” \nAll begin in delight and end in wisdom, as Frost taught us great poems should.Gwendolyn Brooks, “We Real Cool”This blew my mind in high school, and I wasn’t the only one.")
file.close()

file=open("file.txt","r")
print(file.read())
file.close()

