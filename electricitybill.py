unit_1=int(input("Enter the units of domestic purpose:"))
unit_2=int(input("Enter the units of consumer purpose:"))
#Domestic electricity bill
if(unit_1>0)and(unit_1<=200):
  price_1=float(unit_1*6)
elif(unit_1>200)and(unit_1<=300):
  price_1=float(unit_1*8)
else:
  price_1=float(unit_1*10)
print(price_1)
#Consumer electricity bill
if(unit_2>0)and(unit_2<=150):
  price_2=float(unit_2*7)
elif(unit_2>150)and(unit_2<=200):
  price_2=float(unit_2*7.5)
else:
  price_2=float(unit_2*12.30)
print(price_2)