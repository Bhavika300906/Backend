class Calculator:
    def getData(self, num1, num2, operator):
        self.num1 = num1
        self.num2 = num2
        self.operator = operator

    def calculate(self):
        if self.operator == "+":
            result = self.num1 + self.num2
        elif self.operator == "-":
            result = self.num1 - self.num2
        elif self.operator == "*":
            result = self.num1 * self.num2
        elif self.operator == "/":
            if self.num2 == 0:
                result = "Cannot divide by zero!"
            else:
                result = self.num1 / self.num2
        else:
            result = "Invalid operator!"

        print("Result :", result)

c1 = Calculator()
c1.getData(10, 5, "+")
c1.calculate()   # Result : 15

c2 = Calculator()
c2.getData(10, 0, "/")
c2.calculate()   # Result : Cannot divide by zero!
