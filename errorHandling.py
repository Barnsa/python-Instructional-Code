def errorTest():
    while True:
        try:
            variable_a = int(input("please input a number: "))
            variable_b = 5
            
            # When we write an assert statement, you want the assert to be True. 
            # Otherwise, everything after the comma gets printed out as an error message and 
            # the program ends. 
            assert not isinstance(variable_a, str), "input shouldn't be a string here"  #this assert = if not a string then continue, else print; "input shouldn't be a string here"
            # assert (variable_a >= 0), "cannot do modulo operators on negative numbers"
            print(variable_a % variable_b)

        except (TypeError, ValueError):
            print("You didn't enter an integer!")

def KelvinToFahrenheit(Temperature):
    try:
        assert not isinstance(Temperature, str), "Cannot do calculations on a string!"  #this is the same principle as the assert above
        assert (Temperature >= 0),"Colder than absolute zero!"
        return (((Temperature-273)*1.8)+32)
    except:
        print("an unknown exception has been thrown!")

if __name__ == "__main__":
    print (KelvinToFahrenheit(273))
    print ((KelvinToFahrenheit(505.78)))
    print (KelvinToFahrenheit(-5))
    errorTest()