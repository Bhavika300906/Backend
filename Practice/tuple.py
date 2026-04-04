t = (1,2,10,20,"tops",True,[100,200,300],"python",False,1,2,10)
print(t)
print(t.count(1))
print(t.index(10))

for i in t:
    print(i)

print(t[6])
t[6].append(400)
print(t)
