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

def fibonacci1():
    # We start with an empty array
    fib = []

    # We need a counter for the loop
    count = 0

    # This is an example of a "try, except" statement that we use for error checking
    try:
        # This is asking for user input and making sure the value we get back is an integer
        count = int(input("How many digits long would you like your Fibonacci sequence? \n"))

    except:
        # If it's not an integer then, as the exception is thrown, we catch them all here and print out this message
        print("That is not a number!! \n\nExiting!!\n\n")
    
    # This is our "for" loop that is looping for as long as the user has told it to
    for i in range(count):
        # If it's the first time it's counting, then append the first number "0" to the array
        if i == 0:
            fib.append(0)
        # else if it's the second time it's counting then append a "1" to the array
        elif i == 1:
            fib.append(1)
        # Otherwise, we need to count the fibonacci numbers out up to the "count" number
        else:
            fib.append(fib[i-1] + fib[i-2])
    # Then return the whole array to be printed out using "print" later
    return(fib)


def fibonacci2():
    # We start with an empty array
    fib = []

    # Then a counter for your loop
    count = 18  #### This is 2 less than 20 cause we're about to append the first two values before the loop!! ####

    # We create the initial entries in the array so we can count the Fibonacci numbers out, this info came from the Wiki page
    a, b = 0, 1 

    # Then we'll append them into the array
    fib.append(a)
    fib.append(b)

    # While the number is above the count number then we keep calculating and appending the values we need. 
    while count > 0:
        # This looks a little confusing, but all it's doing is making the value of "a = b" and "b = a + b"
        # So, first time around it will make "a = 1" and "b = 1 + 0" at the same time. 
        a, b = b, a + b

        # then we append the new value of b to the array
        fib.append(b)

        # and we decrement "count" so that the while loop doesn't go on forever
        count -= 1

    # Once we've finished calculating then we return the fib array so that it can be printed
    return(fib)


def fibonacci3():
    # This is an example of doing it with a partially filled array just to show that it can be done
    fib = [0, 1]

    # this is the counter so we do 20 loops
    count = 20

    # a "for" loop cause we know the number of times we want to loop
    for i in range(count):
        # cause "fib" is already filled with results we want to wait untill "i" is the same number as the index value of "fib" we are looking for
        if i > 1:
            # This is the same math as in "fibonacci1" 
            fib.append(fib[i-1] + fib[i-2])
    return(fib)


if __name__=='__main__':
    # store the returned value in "a"
    a = fibonacci1()
    # then print it out
    print(a)
    # or we can just print it directly
    print(fibonacci2())
    # I tend to print things out directly
    print(fibonacci3())