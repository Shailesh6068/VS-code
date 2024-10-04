i = 0
# def give():
#     i = i+1
#     print("i :",i)

def output(a, b):
    real = a
    imag = b  
          
    if imag < 0:
        print(real,imag,"i")
    else:
        print(real,"+",imag,"i")  
    
class ComplexNumber:
    def input(self):
        self.a = int(input(f"Write the real part {i} :"))
        self.b = int(input(f"Write the imaginary part {i}:"))
        # give()
        i = i +1
        
    def show(self):
        if self.b < 0:
            print(self.a,self.b,"i")
        else:
            print(self.a,"+",self.b, "i")
        
    def __add__(self, num2):
        real = self.a + num2.a
        imag = self.b + num2.b
        print("i:",i)
        output(real,imag)
        
        
    def __sub__(self, num2):
        real = self.a - num2.a
        imag = self.b - num2.b
        print("i:",i)
        output(real,imag)
           
c1 = ComplexNumber()
c2 = ComplexNumber()
c1.input()
c2.input()
c1.show()
c2.show()
c1+c2
c1-c2
           





