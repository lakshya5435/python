#conditioal expression


num=int(input("enter the number: "))
a=int(input("enter the number:" ))
b=int(input("enter the second number: "))
age=int(input("enter your age"))
temperature=float(input("enter the temperature"))
user_role=input("enter your role")

 
print("Positve" if num>0 else "Negative")  #positive or negative
print("even" if num%2==0 else"odd")         #even or odd
print(a if a>b else b)                      #max number
print(a if a<b else b)                      #min number
print("Adult" if age>18 else "child")       #adult or child
print("hot"if temperature >20 else "Cold")  #hot or Cold
print("Full Access" if user_role=="admin" else "access denied")

