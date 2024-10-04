#FOR PRIVATE ( " __ ") this are use
class Access:
    def __init__(self):
        self.__privateattribut = 5          # This is private attribute 
        self.__name = "ram"
        print(f"The a is {self.__privateattribut} and name is {self.__name}")
        
    def __private(self,a,b):         #this is private function
        self.q = a
        self.w = b
        print(f"The q is {self.q} and w is {b}")

a1 = Access()

# Accessing private attributes directly using name mangling
print(a1._Access__privateattribut)  # This will work, but it's not recommended
print(a1._Access__name)  # This will work, but it's not recommended

# Accessing private method directly using name mangling
a1._Access__private(10, 20)  # This will work, but it's not recommended
        