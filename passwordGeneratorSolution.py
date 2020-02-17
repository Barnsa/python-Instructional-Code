##################################################################################################################################
## Written by: Adam Barns                                                                                                       ##
## Contact: adambarns83@gmail.com                                                                                               ##
## Created as part of an instructional series into Python programming                                                           ##
##                                                                                                                              ##
## Title: Password Generator Solution                                                                                           ##
##                                                                                                                              ##
##################################################################################################################################

# we need 'random' for random generation of characters/data. 
# It's not crypographically sound however, and another library should be used
import random

# All passwords in the english language are made up of these
chars = 'abcdefghijklmnopqrstuvwxyz'
capitols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '1234567890'
special = '!\"£$%^&*\()-+=<>,.@#~\'?/[]\{\}-_' 

def passwordGenerator1():
    # The way most people generate a password is with a word that is usually a name of someone precious to them
    password1 = str(input("Please enter the name of your dog, cat, or favourite person: \n"))
    return password1
    

def passwordGenerator2():
    # we've all been told that we shouldn't do it the way passwordGenerator1 makes a password
    # passwordGenerator2 uses all the rules that we're told to use...
    # "At least 8 characters long with: One capitol letter, one lower case letter, one number and one special character"
    password2 = str(input("Please enter a word that is at least 8 characters long: "))

    # Most people capitalise the first letter, which .capitalize does to a function
    password2 = password2.capitalize()
    password2 = password2 + random.choice(numbers)    
    return password2


def passwordGenerator3():
    # We're told that an even better way to make a password is to make a password with lots of 
    # randomly gererated letters and numbers. This is pretty good for security, but not so good for remembering...
    choices = chars + capitols + numbers + special
    password3 = ''
    for i in range(12):
        password3 = password3 + random.choice(choices)
    return password3        

def passwordGenerator4():
    # The most secure way of generating a password that is both easy to remember and is also secure, 
    # is to take four randomly chosen words and add them together.
    from bs4 import BeautifulSoup
    import requests

    pageLink = 'https://en.wikipedia.org/wiki/List_of_Asian_countries_by_area'

    pageResponse = requests.get(pageLink, timeout = 5)

    soup = BeautifulSoup(pageResponse.content, "html.parser")

    filtered = soup.findAll('a')
    passwordWords = []

    for i in filtered:
        # We isolate the title to make sure that 
        word = i.get('title')

        # This is to eliminate all of the links without titles
        if word is not None:
            passwordWords.append(word)
    
    # We'll make a prettier wordlist using slices
    wordlist = passwordWords[6:(len(passwordWords)-73)]
    
    # variable to hold the final password and the symbol as a word spacer
    password = ''
    simpleSymbols = random.choice(special)
    for word in range(4):
        password = password + random.choice(wordlist)
        if word == 0 or word == 1 or word == 2:
            password = password + simpleSymbols

    return(password)


if __name__ == "__main__":
    password1 = passwordGenerator1()
    print(f"Results from passwordfolder 1: {password1}")
    print( passwordGenerator2() )

    print( passwordGenerator3() )
    print( passwordGenerator4() )