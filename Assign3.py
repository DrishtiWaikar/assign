print("Select Operation to perform:")
print("1.Add\n2.Sub\n3.Multiply\n4.Divide ")

num = int(input("Enter an option you want to choose:"))
if num==1:
    n1=int(input("Enter Num1:"))
    n2=int(input("Enter Num2:"))
    print("Addition  is:",n1 + n2)
elif num==2:
    n1=int(input("Enter Num1:"))
    n2=int(input("Enter Num2:"))
    print("Subtraction is:",n1-n2)
elif num==3:
    n1=int(input("Enter Num1:"))
    n2=int(input("Enter Num2:"))
    print("Multiplication is:",n1*n2)
elif num==4:
    n1=int(input("Enter Num1:"))
    n2=int(input("Enter Num2:"))
    print("Division is:",n1/n2)
else:
    print("Wrong Choice")

        
         


