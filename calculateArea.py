def area (int1, int2):
    total = int1 * int2 
    return total

def payments (amount, interest):
    monthly = (0.0867 * amount)/3
    print(monthly)
    interestAmount = amount + (amount * (interest/100))
    print (interestAmount)
    timeToPay = (interestAmount / monthly)/12
    print(timeToPay)


# 8400
# 13.75
elainesProblem = ( area(220, 140)/area(20, 20) )
print(elainesProblem)
payments(8400, 13.75)