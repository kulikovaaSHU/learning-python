print("Calculator Loading...\n")


def mult(num1, num2):
    return num1*num2


def divd(num1, num2):
    if num2 != 0:
        return num1/num2
    else:
        error_catch(0)


def add(num1, num2):
    return num1+num2


def subs(num1, num2):
    return num1-num2


def mod(num1, num2):
    if num2 != 0:
        return num1%num2
    else:
        error_catch(0)


def calculate(calc):
    num1 = float(input("\nEnter first number: "))
    num2 = float(input("Enter second number: "))
    if calc == "M":
        return mult(num1, num2)
    elif calc == "D":
        return divd(num1, num2)
    elif calc == "A":
        return add(num1, num2)
    elif calc == "S":
        return subs(num1, num2)
    elif calc == "Mod":
        return mod(num1, num2)
    else:
        return "Invalid"


def main_function():
    print("\nPlease select your option: ")
    calc = input("Enter M(multiply), D(divide), A(add), S(subtract) or Mod(mod): ")
    if calc != "M" and calc != "D" and calc != "A" and calc != "S" and calc != "Mod":
        error_catch(1)
    else:
        print("\nResult: " + str(calculate(calc)))
        go_again()


def go_again():
    again = input("\n\nEnter C to continue, enter Q to quit: ")
    if again == "C":
        main_function()
    elif again != "Q":
        error_catch(2)
    elif again == "Q":
        print("\nGoodbye.")


def error_catch(errornum):
    if errornum == 0:
        print("\nError: can't divide by 0.")
        main_function()
    elif errornum == 1:
        print("\nInvalid Input, try again.")
        main_function()
    elif errornum == 2:
        print("\nInvalid input. Try again.")
        go_again()


main_function()
print("\n...Shutting down")