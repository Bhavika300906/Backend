#Without Arguments - super Class

'''class A:
    def show(self):
        print("Show From A")

class B(A):
    def show(self):
        super().show()
        print("Show From B")

class C(A):
    def show(self):
        super().show()
        print("Show From C")

class D(C,B):
    def show(self):
        super().show()
        print("Show From D")

d1=D()
d1.show()'''


#With Arguments- super Class

class A:
    def show(self,a):
        print("Show From A : ",a)

class B(A):
    def show(self,a):
        super().show(20)
        print("Show From B : ",a)

class C(A):
    def show(self,a):
        super().show(30)
        print("Show From C : ",a)

class D(C,B):
    def show(self,a):
        super().show(40)
        print("Show From D : ",a)

d1=D()
d1.show(10)



        
