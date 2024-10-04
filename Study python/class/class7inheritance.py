class parent:
    def p(self):
        self.q = 5
        print("Parent : ",self.q) 

class child(parent):
    #def q(self):
    def p(self):
        print("Child. ")
      #  super().p()                      # method 1

c = child()
# w = parent()                            #method 2 make differnt object of parent class
# w.p()
c.p()

