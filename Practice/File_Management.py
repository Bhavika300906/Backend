file = open("tops1.txt","w")
file.write("This is file management demo using python.")
file.close()
print("File Written Successfully")
print("*"*50)

file=open("tops1.txt","a")
fil

file = open("tops1.txt","r")
print(file.read())
file.close()
print("*"*50)


file = open("tops1.txt","r")
print(file.read())
file.close()
print("*"*50)

file=open("tops2.txt","w+")
file.write("This is w+ operation in python.")
print("File Current Position: ",file.tell())
file.seek(15)
print("File Data : ", file.read())
file.close()
print("*"*50)
