# Program #2: Word Separator
# Write a program that accepts as input a sentence in which all of the words are run together, 
# but the first character of each word is uppercase.  
# Convert the sentence to a string in which the words are separated by spaces, 
# and the first word starts with an uppercase.  
# For example the string "StopAndSmellTheRoses" would be converted to "Stop and smell the roses."


#Tanner Rosenthal
#3/19/25
#Sentence Fixer

sentence = input("enter a sentence in camel case")

def fix_sentence(sentence):
    fixed_sentence = sentence[0].upper()
    for char in sentence[1:]:
        if char.isupper():
            fixed_sentence += " " + char.lower()

        else:
            fixed_sentence += char

    print(fixed_sentence)

print("Your sentence can be written as: ")
fix_sentence(sentence)
