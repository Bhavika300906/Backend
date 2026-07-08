file = open("demo1.txt","w")
file.write("This is file management using Python")
file.close()
print("File Written Successfully")

file = open("demo1.txt","r")
content = file.read()
print("File Content : ", content)
file.close()

