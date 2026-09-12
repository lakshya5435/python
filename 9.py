#functions

import math

radius=float(input("enter the radius of a circle: "))

circumference=2*math.pi*radius

print(f"the circumference is:{round(circumference,2)}cm")

radius=float(input("enter the radius of a circle:"))

area=math.pi *pow(radius,2)

print(f"the area of a circle is: {round(area,2)}cm^2")

a=float(input("enter the side A: ")) 
b=float(input("enter the side B: "))
c=math.sqrt(pow(a,2)+pow(b,2))
print(f"the hypotenuse of the triangle is: {round(c,2)}cm")
