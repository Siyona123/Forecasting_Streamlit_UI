from exc import input_number

def division(x,y):
    try:
        c=x/y
        return c
    except ZeroDivisionError:
        print("division by zero is not posible")


num1=input_number("Num 1 :")
num2=input_number("Num 2 :")

print(division(num1,num2))