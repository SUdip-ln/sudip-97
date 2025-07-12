#1. Indexing and Slicing
# Given the string s = "PythonPractice", what are the outputs of:
#- s[1]
#- s[-3:]
#- s[2:7]

s="pythonpractice"

print(s[1])
print(s[-3:])
print(s[2:7])

#2. Reverse a String
#Write a one-liner to reverse the string "developer" using slicing.
string="developer"
print(string[::-1])

#3. Count Vowels
#Write a function that counts the number of vowels in a given string
def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)
print(count_vowels("developers"))

#4. Check for Palindrome
#Write a function to check if a given string is a palindrome. Ignore spaces and capitalization.
def is_palindrome(s):
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]
print(is_palindrome("A man a plan a canal Panama"))

#5. Clean and Format String
#Given text = "   hello world! welcome to Python.   ", write code to:
# Remove leading/trailing spaces
#- Capitalize each word
#- Replace the word "Python" with "Programming"
text = "   hello world! welcome to Python.   "
text = text.strip()  
text = text.title()  
text = text.replace("Python", "Programming") 
print(text)

#6.  Find Longest Word
#Write a function that takes a sentence and returns the longest word in it.
def find_longest_word(sentence):
    words = sentence.split()
    longest_word = max(words, key=len)
    return longest_word
print(find_longest_word("I'm going to college daily")) 

#7.  String Operators
#Given s1 = "Py" and s2 = "thon", what are the results of:
#- s1 + s2
#- s1 * 3
#- "y" in s1
s1 = "Py"
s2 = "thon"
print(s1 + s2)  
print(s1 * 3)   
print("y" in s1)

#8. Remove Duplicate Characters
#Write a function that removes all duplicate characters from a string but keeps the first occurrence.
def remove_duplicates(text):
    result = ""
    for char in text:
        if char not in result:
            result += char
    return result
print(remove_duplicates("programming"))



