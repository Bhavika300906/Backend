d={}
n=int(input("Enter N: "))
sum=0

for i in range (1,n+1):
    d[i]=i*i
    sum=sum+d[i]
print(d)
print("Sum : ",sum)
