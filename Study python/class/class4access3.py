#FOR PROTECTED ( " _ ") this are use           // this are use in inheritance. \\
class access:
    def __init__(self):
        self._protectedattribut = 5          # This is protected attribute 
        self._name = "ram"
        print(f"The a is {self.__protecteda} and name is {self.__name}")
        
    def _protected(self,a,b):         #sthis is protected function
        self.q = a
        self.w = b
        print(f"The q is {self.q} and w is {b}")

a1 = access
print(a1.__protectedattribut)
a1.__protecteda