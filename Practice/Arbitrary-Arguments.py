def test(a,b,c,*d):
    print("A : ",a ,"B : ",b ,"C : ",c ,"D : ",d)

test(3,4,5,6,7,8,9,0,12,34) #*d Used to create tuple

def test(a,b,c,*d):
    print("A : ",a ,"B : ",b ,"C : ",c ,"D : ",list(d)) #create list

test(3,4,5,6,7,8,9,0,12,34) #*d Used to create tuple

