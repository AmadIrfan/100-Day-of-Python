import colorama as color
from colorama import Fore
import operator as op


def operator(color):
    print(color, " + for Plus \n - for Subtract \n / for division \n * for Multiplication ", Fore.WHITE)


def inputOne():
    try:
        inputOne = input("Enter a number ")
        return int(inputOne)
    except:
        print(Fore.RED, " \t  Wrong input \n \t Please Enter numbers between 0 to 9 ", Fore.WHITE)


def inputTwo():
    try:
        inputTwo = input("Enter a number ")
        return int(inputTwo)
    except:
        print(Fore.RED, " \t  Wrong input \n \t Please Enter numbers between 0 to 9 ", Fore.WHITE)


def inputOperator():
    try:
        inputOp = input("Enter an operator ")
        return str(inputOp)
    except:
        print(Fore.RED, 'Wrong Operator \n ')
        operator(Fore.RED)


def inputResult():
    result = 00
    operator(Fore.GREEN)
    one = inputOne()
    opr = inputOperator()
    two = inputTwo()
    if opr == "+":
        result = (one+two)
    elif opr == "-":
        result = (one-two)
    elif opr == "*":
        result = (one*two)
    else:
        result = (one/two)

    print("result is " + str(result))


print(5/5)
