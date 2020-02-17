##################################################################################################################################
## Written by: Adam Barns                                                                                                       ##
## Contact: adambarns83@gmail.com                                                                                               ##
## Title: Fibonnacci Sequence Generators                                                                                        ##
## Created as part of an instructional series into Python programming                                                           ##
##                                                                                                                              ##
## What does it do:                                                                                                             ##
## Program to count the Fibonacci sequence and print it out to console, this was done in more than one style for reflective     ##
## learning. The task was outlined as:                                                                                          ##
##                          - Create an empty array                                                                             ##
##                          - Using a loop, append the values of the fibonacci sequence into the array                          ##
##                          - print out the values of the array out to the console                                              ##
##                                                                                                                              ##
##                                                                                                                              ##
##################################################################################################################################


def userInput():
    # We need a counter for the loop in our other functions
    count = 0

    # This is an example of a "try, except" statement that we use for error checking
    try:
        # This is asking for user input and making sure the value we get back is an integer
        count = int(input("How many digits long would you like your Fibonacci sequence? \n"))

    except:
        # If it's not an integer then, as the exception is thrown, we catch them all here and print out this message
        print("That is not a number!! \n\nExiting!!\n\n")
    return(int(count))


def fibonacci(count):
    # This is a direct copy of "fibonacci3" in the previous example
    fib = [0, 1]
    for i in range(int(count)):
        if i > 1:
            fib.append(fib[i-1] + fib[i-2])
    return(fib)


if __name__ == "__main__":
    print(fibonacci(userInput()))
