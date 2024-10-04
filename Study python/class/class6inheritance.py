class parent:                           
    def __init__(self, w):
        self.a = w
        self.b = "parent"
        print("I am a Parent")   
    
    def p(self):
        self.q = 5
        print("Parent : ", self.q)

class child(parent):

    def __init__(self):                 # Call the parent class constructor                                     
        print("Child.")                 # Initialize child class attribute

    def p(self,w):
        super().__init__(w)
        self.w = w
        print("Child : ", self.w)

c = child()                             # Creating an object of the child class
c.p(5)                                  # Calling the overridden p() method of the child class

#  This happens because Python looks for the method 
#  in the class of the object itself (child class in this case) before looking in the parent classes.