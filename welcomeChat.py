##################################################################################################################################
## Written by: Adam Barns                                                                                                       ##
## Contact: adambarns83@gmail.com                                                                                               ##
## Created as part of an instructional series into Python programming                                                           ##
##                                                                                                                              ##
## Title: input / output                                                                                                        ##
##                                                                                                                              ##
## Program something that can take input from a user and have a short conversation with a user. Run the test code included to   ##
## see an example. The task is outlined as:                                                                                     ##
##                          - Use 'input' to gather and store a bunch of user supplied information.                             ##
##                          - Find a way to test that the code is working using 'try' statements.                               ##
##                          - Talk back to a user and try to have a realistic speaking experience (if a little basic).          ##
##                  Advanced:                                                                                                   ##
##                          - Store all of the variables in a file to recall them later.                                        ##
##                          - Search through the user supplied text to find conversation topics (start of interactivity)        ##
##                          - Program it using object orientated programming (use classes) to create a bot for multiple users.  ##
##                                                                                                                              ##
##################################################################################################################################

import time

def testCode():

    affirmative = ['YEAH', 'YES', 'OK', 'MAYBE', 'SORT OF', 'KIND OF', 'A BIT']
    try:
        name = str( input("What's your name?\n") )
        age = int( input(f"It's lovely to meet you {name}, I wonder if I might trouble you for your age?\n") )
        if age < 50:
            print(f"{age} isn't very old is it?!\n")
        elif age == 50:
            print("Half a century old!! With age comes wisdom, with wisdom comes enlightenment.\n")
        else:
            print(f"It's a good job people are like a fine wine, cause you are approaching becoming the finest at {age} years old!!.\n")

    except:
        print("A conversation can't be had if you won't take this seriously!!\n")
        
    try: 
        wait(3)
        playSports = str( input("So do you play any sports?\n") )
        playSportsFlag = 0
        for i in range( len(affirmative) ):
            if playSports.upper == affirmative[i]:
                playSportsFlag = 1
        
        if playSportsFlag == 1:
            

    except:    


if __name__ == "__main__":
    testCode()