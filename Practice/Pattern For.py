'''i=5
j=5
for i in range (1,6,1):
    print(*)
for j in range (6,0,-1):
    print()'''

for i in range(1,10):
    for j in range(1,i+1):
        print("*",end="")
    print()

for i in range(1,10):
    print("*" *i)


for i in range (1,10):
    print(" "*(9-i),"*"*i)
    
for i in range (1,10):
    print(" "*(9-i)," *"*i)
