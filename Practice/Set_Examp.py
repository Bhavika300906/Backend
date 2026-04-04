
# SET
my_set = {1,2,3}
my_set.add(4)
print(my_set)


# Difference
set1={1,2,3}
set2= {3,4,5}

#difference_set= set1 - set2 # set1.difference(set2)
#difference_set= set1 & set2 # set1.difference(set2) #comman no. is output
#difference_set= set1 ^ set2 # set1.difference(set2) #uncomman no. is output
difference_set= set1 | set2 # set1.difference(set2) #All No. is output
print(difference_set)


#list converted into Set

my_set = {1,2,3,4}
my_set2= set([1,2,1,2])
print(my_set)
print(my_set2)


# Discard Fun
my_set = {1,2,3,4}

my_set.remove(2)
my_set.discard(10)
print(my_set)
