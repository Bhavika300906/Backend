#Function With NO argument no rerurn
def printLine():
    print("*"*50)

printLine()
print("Welcome To UDF in python.")
printLine()

#Functon with argument and no return

def add(a,b):
    print("Add: " , a+b)

printLine()
add(10,20)
printLine()

#Function with argument & return value

def sub(a,b):
    return a-b
printLine()
print("SUB: " , sub(10,20))
#ans=sub(10,20)
#print("Sub: ", ans)
printLine()
