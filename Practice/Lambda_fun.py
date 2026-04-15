def cube(x):
    return x*x*x
print("Cube of 5 is : ",cube(5))

ans=lambda y:y*y*y
print("Cube of 5 is : ",ans(5))

x=lambda a,b:a+b
print(x(10,20))


def oddeven(a):
    if a%2==0:
print(a," is Even")
    else :
print(a," is Odd")

oddeven(5)

y=lambda a:"Even" if a%2==0 else "Odd"
print(y(1))
