class rectangle:
    def __init__(self,a,b):
        self.q = a
        self.w = b
        #r = self.q + self.w                   rectangle' object has no attribute 'r'
        self.r = self.q + self.w
        print("a + b :",self.r)
        print(f"The value is {self.q} and {self.w}")

rectangle1 = rectangle(4,3)        #Creating Object and calling constructor
rectangle2 = rectangle(7,8) 
rectangle3 = rectangle(1,2) 
print(rectangle1.r)
