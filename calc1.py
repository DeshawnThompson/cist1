from calc_one import add,sub,divide,multiply,mod
def userinput():
    number1,number2 = getnum()
    operation = input("+,-,/,%,x  ?: ")
    if operation == "+":
        Total = add(number1,number2)
        print(Total)
    elif operation == "-":
        Total = sub(number1,number2)
        print(Total)
    elif operation == "/":
        Total = divide(number1,number2)
        print(Total)
    elif operation == "x":
        Total = multiply(number1,number2)
        print(Total)
    elif operation == "%":
        Total = mod(number1,number2)
        print(Total)

    
def getnum():
    number1 = int(input(" enter number 1: "))
    number2 = int(input("enter number 2: "))
    return(number1, number2)

userinput()