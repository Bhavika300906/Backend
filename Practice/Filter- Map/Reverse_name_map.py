def reverse_string(name):
    return name[ : :-1]

namelist= ["Niky","Diya","Bhavika","Niyati", "Khushi"]

reverseName = map(reverse_string,namelist)
print("-" * 80)
print("Original List : ", namelist)
print("-" * 80)
print("Reverse Name List : ",list(reverseName))
print("-" * 80)

list1=[]
for i in namelist:
    j= reverse_string(i)
    list1.append(j)


#print(list1)
