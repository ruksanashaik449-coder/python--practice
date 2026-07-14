salary=int(input("Enter your salary:"))
if(salary>=10000) and (salary<20000):
  loan_amount=100000
  print("Eligible for loan:",loan_amount)
  annual_interest=12
  duration=20
  interest=annual_interest/(12*100)
  emi=(loan_amount*interest*(1+interest)**duration)/(((1+interest)**duration)-1)
  print("The EMI should paid:",emi)
elif(salary>=20000) and (salary<30000):
  loan_amount=300000
  print("Eligible for loan:",loan_amount)
  annual_interest=12
  duration=20
  interest=annual_interest/(12*100)
  emi=(loan_amount*interest*(1+interest)**duration)/(((1+interest)**duration)-1)
  print("The EMI should be paid:",emi)
elif(salary>=30000) and (salary<50000):
  loan_amount=500000
  print("Eligible for loan:",loan_amount)
  annual_interest=24
  duration=60
  interest=annual_interest/(12*100)
  emi=(loan_amount*interest*(1+interest)**duration)/(((1+interest)**duration)-1)
  print("The EMI should be paid:",emi)
elif(salary>=50000):
  loan_amount=int(input("Enter theloan amount between 500000 to 1500000:"  ))
  if(loan_amount>=500000)and(loan_amount<=1500000):
    print("Eligible for loan:",loan_amount)
    annual_interest=16
    duration=72
    interest=annual_interest/(12*100)
    emi=(loan_amount*interest*(1+interest)**duration)/(((1+interest)**duration)-1)
    print("The EMI should be paid:",emi)
else:
  print("Not Eligible for loan")