sname =input("Enter Student name: ")
rno =int (input("Enter Student Roll No: "))
s1 = int (input("Enter Marks of S1: "))
s2 = int (input("Enter Marks of S2: "))
s3 = int (input("Enter Marks of S3: "))

total =s1+s2+s3
per =total/3

print("Student name: ",sname)
print("Total: ",total)
print("Per: ",per)

if per>=70:
    print("Distintion")
elif per>=60:
    print("Fisrt")
elif per>=50:
    print("Second")
elif per>=40:
    print("Pass")
else:
    print("Fail")
