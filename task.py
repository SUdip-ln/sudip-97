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