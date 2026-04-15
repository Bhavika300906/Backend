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

class D(A):
    def getD(self,d):
        self.d=d
    def putD(self):
        print("D:", self.d)


b=B()
c=C()
d=D()

c.getA(10)
b.getB(20)
c.getC(30)
d.getD(40)
c.putA()
b.putB()
c.putC()
d.putD()
 

