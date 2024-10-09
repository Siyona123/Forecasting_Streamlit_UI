def input_number(prompt):
    while True:
        try:
            inp=int(input(prompt))
            return inp
        except:
            print("value is incorrect,please type again")
        else:
            print("Thankyou for entering this value")    



# input1=input_number("Enter first num:")
# input2=input_number("Enter second num:")
# print(input1+input2)
