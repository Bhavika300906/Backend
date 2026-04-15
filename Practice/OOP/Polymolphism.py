class Base:
    def show(self):
        print("Show From Base Class")

class Derived(Base):
    def show(self):
        super() .show()
        print("Show From Derived Class")

class SubDerived(Derived):
    def show(self):
        super() .show()
        print("Show From SubDerived Class")
        
s1=SubDerived()
s1.show()

