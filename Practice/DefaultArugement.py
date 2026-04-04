def test(a=40,b=40,c=30,d=50):
    print("a: ",a,"b: ",b,"c: ",c,"d: ",d)

test()

def test1(a,b,c,d):
    print("a: ",a,"b: ",b,"c: ",c,"d: ",d)

test1(10,20,30,40)

def test2(a=40,b=40,c=30,d=50):
    print("a: ",a,"b: ",b,"c: ",c,"d: ",d)

test2(b=80,d=100) #priority of calling argument is more than the given argument in function

