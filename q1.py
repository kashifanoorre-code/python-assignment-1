#Problem 1: Arithmetic Operations ( Using Functions )

num1=int(input("enter your first number: "))
num2=int(input("enter your second number: "))

def add(num1,num2):
    return num1+num2

def multi(num1,num2):
    return num1*num2

def divide(num1,num2):
    if(num2==0 or num1==0):
        print("please enter valid number!")
    else:
        return num1/num2

def sub(num1,num2):
    return num1-num2

op=int(input("enter 1 for addition, 2 for subtraction, 3 for multiplication and 4 for division"))
match op:
    case 1:
        print("result is = ", add(num1,num2))
    case 2:
        print("result is = ", sub(num1,num2))
    case 3:
        print("result is = ", multi(num1,num2))
    case 4:
        print("result is = ", divide(num1,num2))