num1=float(input("Enter your first number:"))
num2=float(input("Enter your second number:"))
print("1.Addition")
print("2.Subraction")
print("3.Multiplication")
print("4.Division")
choice=int(input("Enter your choice:"))
if choice==1:
    result=num1+num2
    print(result)
elif choice==2:
    result=num1-num2
    print(result)
elif choice==3:
    result=num1*num2
    print(result)
elif choice==4:
    if num2==0:
        print("Cannot divide by 0")
    else:
        result=num1/num2
        print(result)  
else:
    print(result)         

