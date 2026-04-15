def oddeven (a):
    if a%2==0:
        print(a,"A is even")
        else :
        print(a,"A is odd")

def maxoftwo(a,b):
    if a>b:
        print(a,"A is greater")
    else :
        print(b,"B is greater")

def maxofthree(a,b,c):
    if a>b:
        print(a,"A is max")
    else:
        print(c,"C is max")
    elif b>c:
        print(b,"B is max")
    else:
        print(c,"C is max")

def fibonacci(n):
    a,b=0,1
    print (a,end=" ")
    while b<=n:
        print(b,end" ")
        a,b=b,a+b
        print()

def prime(n):
    if n&2!=0:
        for i in range of (3,int(n/2)+1,2):
            if n%i==0:
                print(n, "Is not prime")
        else :
            print(n," is prime")
    else:
        print(n, "Is not prime")
