import math
def isEven(num1):
    the_result = num1 % 2 ==0
    return the_result

def isOdd(num1):
    the_result = num1 % num2 == 1
    return the_result
def main():
    the_number = int(input("Enter a number"))
    if(isEven(the_number)):
        print("its even")
    elif(isOdd(the_number)):
        print("its odd")

main()