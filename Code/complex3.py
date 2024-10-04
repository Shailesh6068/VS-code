class ComplexNumber:
    i = 0  # Initialize i as a class variable
    k = 1

    @staticmethod
    def output(real, imag):       
        if imag < 0:
            print(real, imag, "i")
        else:
            print(real, "+", imag, "i")
    
    def __init__(self):
        ComplexNumber.i = ComplexNumber.i + 1

    def input(self):
        w = ComplexNumber.i
        self.a = int(input(f"Write the real part {w}: "))
        self.b = int(input(f"Write the imaginary part {w}: "))
      
    def show(self):
        l = ComplexNumber.k
        print(f"The {l} Written by you :")      
        if self.b < 0:
            print(self.a, self.b, "i")
        else:
            print(self.a, "+", self.b, "i")
        ComplexNumber.k = ComplexNumber.k + 1

    def __add__(self, num2):
        real = self.a + num2.a
        imag = self.b + num2.b
        ComplexNumber.output(real, imag)

    def __sub__(self, num2):
        real = self.a - num2.a
        imag = self.b - num2.b
        result = ComplexNumber()
        result.output(real, imag)


    def __mul__(self,num2):
        real = (self.a*num2.a)-(self.b*num2.b)
        imag =(self.a*num2.b)+(self.b*num2.a)

        result = ComplexNumber()
        result.output(real,imag)

    def __truediv__(self,num2):
        res = (self.a * num2.a)+(self.b* num2.b)
        im = (self.b * num2.a) - (self.a * num2.b)
        deno = (num2.a*num2.a)+( num2.b*num2.b)
        real = res/deno
        imag = im/deno
        
        result = ComplexNumber()
        result.output(real , imag)

c1 = ComplexNumber()
c1.input()
c2 = ComplexNumber()
c2.input()
c1.show()
c2.show()
print()
print("1:Addition. \n"
      "2:Substraction.\n"
      "3:Multiplication.\n"
      "4:Division.\n")

q = "Yes" 
while q == "Yes":
    w = int(input("Write the choice of following: "))
    
    if w == 1:
        print("Sum:")
        c1 + c2
        
    if w == 2:
        print("Difference:")
        c1 - c2
   
    if w == 3:
        print("Multiplication :")
        c1 * c2
   
    if w == 4:        
        print("Division :")
        c1/c2

    q = input("Do you wan't continue again ('Yes'/'No') :")