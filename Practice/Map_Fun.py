def cube (x):
    return x*x*x
l=[1,2,3,4,5,6,7,8,9]

ans=map(cube,l)

print(list(ans))

l1=[]
for i in range (1,10):
    j=cube(i)
    l1.append(i)

print(l1)
