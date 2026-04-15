class A:
    def getA(self,a):
        self.a=a
    def putA(self):
        print("A :",self.a)

class B(A):
    def getB(self,b):
        self.b=b
    def putB(self):
        print("B :" ,self.b)

class C(A):
    def getC(self,c):
        self.c=c
    def putC(self):
        print("C :", self.c)

class D(B,C):
    def getD(self,d):
        self.d=d
    def putD(self):
        print("D:", self.d)


d=D()

d.getA(10)
d.getB(20)
d.getC(30)
d.getD(40)
d.putA()
d.putB()
d.putC()
d.putD()







