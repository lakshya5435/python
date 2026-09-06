#area of ractangle 
length=float(input("enter the length:"))
width=float(input("enter the width:"))
area=length*width

print(f"the area is {area}cm²")


#shopping cart 

item=input("what item would you like to buy?")
price=float(input("what is the price ?"))
quantity=int(input("how many would you like?"))
total=price*quantity
print(f"you have bought {quantity} x {item}/s")
print(f"your total is ${total}")

