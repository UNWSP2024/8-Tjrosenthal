# Program #1: Initials
# Write a program that gets a string containing a person's first, middle, and last names, 
# and displays their first, middle, and last initials.  
# For example, if the user enters John William Smith, the program should display J. W. S.

#Tanner Rosenthal
#3/19/25
#Initials

def split_initials(name):
    name = name.split()

    for words in name:
        print(f"{words[0].upper()}.", end='')
        


full_name = input("What is your full name?")
print("Your initals are ", end='')

split_initials(full_name)
