# yat funnction inherite hot aahe pan constructor inherite nahi hot tyamule 
# tyatil member aapn access karu shakat nahi . mhanun " super().__init__" vaprun
# tyala inherit karayach 

class parent:                           
    def __init__(self,w):
        self.a = w
        self.b ="parent"
        print("I am a Parent")

    def p(self):
        self.q =5
        print("Parent : ",self.q)

class child(parent):
    def __init__(self,e,w):
        super().__init__(w)        # it is required to inherite the constructor of parent in child
        print("I am a child")

#p = parent(5)
c = child(10,5)
print(c.a)       # aceess parent class atribute
c.p()
