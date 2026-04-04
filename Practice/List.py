l = [10,20,30,"tops",True, 20, "abcd",1.0,2.2,3.3,False,1000,2000,3000]

print(l)
l.append(100)
print(l)
l1=l.copy()
print(l1)
l1.append(200)
print(l)
print(l1)
l2=l
print(l2)
l2.append(300)
print(l)
print(l2)
print(l.count(1))
l3=[1000,2000,5000]
l.extend(l3)
print(l)
print(l.index(5))
l.insert(1,301)
print(l)
      
#l.clear()
#print(l)
