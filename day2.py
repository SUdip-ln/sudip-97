#String data types
#lists and tuples
# conditionals

#slicing
name="sudip"
print(name[0:3])
print(name[0:2])
remove=name[1:3]
print(remove)

#length

print(len(name))

# find and replace # name  letter replacce
print(name.find("d"))
replaced=name.replace("d","p")
print(replaced)

#escape sequence character
text= "my name is sudip \n \'here\' and \ni'm 19 years  old"
print(text)

#write a program to detect double space in a string
text = input ("enter a string ")
if " " in text:
    print("double space detected")
else:
    print("No double space found")



#replace the double space from problem 3 with single spaces

text=input("enter a string")
fixed_text=text.replace(" "," ")
print("fixed string:",fixed_text)

