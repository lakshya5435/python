#weight converter

weight=float(input("enter your weight: "))
unit =input("kilogram or powder?(K or L)")

if unit=="K" or unit=='k':
    weight=weight*2.205
    unit='llbs.'
    print(f"your weight is:{round(weight,2)} {unit}")
elif unit =="L" or unit =='l':
    weight=weight/2.205
    unit='kgs'
    print(f"your weight is:{round(weight,2)} {unit}")
else:
    print(f"{unit} was not valid")



#temp convertion

unit=input("is this temperature in celsius or fahrenheit (C/F): ")
temp=float(input("enter the temperature: "))

if unit=='C'or unit=='c':
    temp=round((9*temp)/5+32,2)
    print(f"the temperature in fahrenheit is:{temp}°F")
elif unit=='f'or unit=='F':
    temp=round((temp-32)*5 /9,2)
    print(f"the temperature in celsius is :{temp}°C")
else:
    print(f"{unit}is an invalid unit of measurement")
