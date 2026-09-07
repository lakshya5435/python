#calculator


operator=input("enter an operator (+,-,*,/): ")

num1=float(input("enter the first number: "))
num2=float(input("enter the second number: "))


if operator =="+":
    print(round(num1+num2,2))
elif operator =="-":
    print(round(num1-num2,2))
elif operator =="*":
    print(round(num1*num2,2))
elif operator =="/":
    print(round(num1/num2,2))
else:
    print("enter a valid operator")
 