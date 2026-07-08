file = open("example2.txt","w+")
file.write("This is python w+ operation demo")
print("File current position :", file.tell())
file.close()
