import UDF_Lib

while True:
    print("*"*40)
    print("1. OddEven")
    print("2. Max of 2 No. ")
    print("3. Max of 3 No. ")
    print("4. Fibonacci ")
    print("5. Prime ")
    print("6. Exit ")
    print("*"*40)
    choice =int(input("Enter Your Choice : "))
    print("*"*40)

    if choice ==1:
        n1=int(input("Enter No. : "))
        UDF_Lib.oddeven(n1)
        
    elif choice ==2:
        n1=int(input("Enter No. : "))
        n2=int(input("Enter No. : "))
        UDF_Lib.maxoftwo(n1,n2)

    elif choice ==3:
        n1=int(input("Enter No. : "))
        n2=int(input("Enter No. : "))
        n3=int(input("Enter No. : "))
        UDF_Lib.maxofthree(n1,n2,n3)
        
    elif choice ==4:
        n1=int(input("Enter No. : "))
        UDF_Lib.fibonacci(n1)
        
    elif choice ==5:
        n1=int(input("Enter No. : "))
        UDF_Lib.prime(n1)

        
    elif choice ==6:
        print("Thank You For Using Us")
        print("*"*40)
        break
    
    else:
        print("Invalid Choice. Try Again")
        print("*"*40)
