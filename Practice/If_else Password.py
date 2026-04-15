reset_pass=None

password=input("Enter the password: ")
print(f"Your password is {password}")

Attemps=3
while True:
    

    user=input("Please enter your password: ")
    print(user)
    if password != user :
        print("Wrong Password! Please try again\n")
        Attemps-=1
        print(f"You can Attempts {Attemps}time's\n")

        if Attemps==0:
            print("You can only 3 time's attampt")
            print("Your password is blocked")
            # break
            print("Please reset Your password\n")
            reset_pass=input("Reset your password: ")
            print(f"Reset password is {reset_pass}")

            if reset_pass==password:
                print("Please change the password ")
            else:
                print(f"Your Reset password is {reset_pass}")
    
    
    elif password==user:
        print("Password is right! You can login I'd\n")
        break

    else:
        break
