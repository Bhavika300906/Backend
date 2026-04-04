l1= [1,2,3,4,5,6,7]
l2=[2,4,5,6,8,9,10]
l3=[]
for i in l1:
    if i in l2:
        pass
    else:
        l3.append(i)

print(l3)
