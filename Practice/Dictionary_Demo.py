d = {101:"Diya", 345:"Bhavika",909:"Niyati",556:"Om",234:"Pralaj",787:"Monik",454:"Parth"}

print(d)
print(d[909])
print(d.get(101))
print(d.items())
print(d.keys())
print(d.values())
print(d.pop(556))
print(d)
print(d.popitem())
print(d)
d1={454:"Parth",556:"Om"}
d.update(d1)
print(d)
d[202]="Kaushal"
print(d)
#d[101]="Jigar"
#print(d)
for i in d:
    print(i, " : ",d[i])
