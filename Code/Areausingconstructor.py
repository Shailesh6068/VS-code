class rectangle:
    # def __init__(self):       #Default type constructor 
    #     self.width = 5
    #     self.height = 6
    #     print("The width and height is :",self.width,self.height)
        
    def __init__(self,width,height):                                    #constructor is calling
        print("The width and height is:",width,height)                  #in python cant call multiple init
        self.width = width
        self.height = height
        print("The width and height is:",self.width,self.height)
        
    # def set_dimension(self,width,height):
    #     self.width = width
    #     self.height = height
    #     print("The width and height is :",self.width,self.height)

    def area(self):
        return self.width*self.height

    def perimeter(self):
        return 2*(self.width+self.height)

rectangle1 = rectangle(4,3)
rectangle2 = rectangle(7,8)
rectangle3 = rectangle(1,2)
#rectangle1.set_dimension(4,6)
# print("The area is:",rectangle1.area())
# print("The perimeter is:",rectangle1.perimeter())