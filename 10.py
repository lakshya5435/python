#if else statement

age=int(input("enter your age: "))

if age>=18:
    print("you are signed up")

elif age<0:
    print("you haven't been born yet")

else:
    print("you must be 18+ to sign up")

response = input("would you like food? (Y/N)")

if response == "Y":
    print("have some food")
elif response =="y":
    print("have some food")
elif response =="n":
    print("no food for you!")
elif response =="N":
    print("no food for you!")
else:
    print("invalid response")



name=input("enter your name: ")

if name == "":
    print("you did not type in your name")
else:
    print(f"hello{name}")




for_sale = True

if for_sale:
    print("this item is for sale")
else:
    print("this item is not for sale")

online= True
if online:
    print("the user is online!")
else:
    print("the user is offline!")
    
    