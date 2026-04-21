from abc import ABC,abstractmethod

class RBI(ABC):

    @abstractmethod
    def roi(r):
        pass


class SBI(RBI):

    def show(self):
        print("This is SBI")

    def roi(self,a):
        print("Rate of Intrest given by SBI is : ",a)

class HDFC(RBI):

    def show(self):
        print("This is HDFC")

    def roi(self,b):
        print("Rate of Intrest given by HDFC is : ",b)

s=SBI()
s.show()
s.roi(6.9)

h=HDFC()
h.show()
h.roi(6.9)

