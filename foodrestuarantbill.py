bill=int(input("Enter the original bill amount:"))
gst=bill*5/100
bill=gst+bill
if(bill>0) and (bill<=2000):
  bill=float(bill-(4/100*bill))
elif(bill>2000) and (bill<=3000):
  bill=float(bill-(7/100*bill))
elif(bill>3000) and (bill<=5000):
  bill=float(bill-(10/100*bill))
else:
  bill=float(bill-(13/100*bill))
print("The final bill with discount:",bill)