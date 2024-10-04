class sample:
    name = "Class method"
    age = 23
       
    def fun(self,method):
        #self.name = method
        #sample.name = method           # Method 1 
        self.__class__.name = method    # Method 2 

    @classmethod                        # Method using class method
    def fun1(cls , age1):
        cls.age = age1
 
s1 = sample()
s1.fun("Ramesh")        
print(s1.name)
print(sample.name)   # here we wan't to print class method but it give problem to solve this we can make.

s1.fun1(25)
print(s1.age)       # call by object
print(sample.age)   #call by class name