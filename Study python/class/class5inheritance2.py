class parent:                           
    def __init__(self):
        self.a = 42
        self.b ="parent"
        print("I am a Parent")

    def p(self):
        self.q =5
        print("Parent : ",self.q)

class child(parent):
    #def __init__(self,e,w):
    def __init__(self):
        super().__init__()        # it is required to inherite the constructor of parent in child  yacha position var depend asate kuthe print vhayache te
        print("I am a child")

#p = parent(5)
#c = child(10,11)
c = child()
print(c.a)       # aceess parent class atribute
c.p()