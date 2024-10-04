class rectangle:

    def set_dimension(self,width,height):
        self.width = width
        self.height = height
        print("The width and height is :",self.width,self.height)

    def area(self):
        return self.width*self.height

    def perimeter(self):
        return 2*(self.width+self.height)

rectangle1 = rectangle()
rectangle1.set_dimension(4,6)

print("The area is:",rectangle1.area())
print("The perimeter is:",rectangle1.perimeter())