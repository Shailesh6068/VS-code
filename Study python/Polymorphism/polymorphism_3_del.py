class parent:
    def __init__(self):
        self.name = " Rajesh "

p1 = parent()
p2 = parent()
print("Name is :",p1.name)
#del(p1)                                        #Deleting the instance 'p1'
del p1
#print("Name after delete is :",p1.name)
del p2.name                                    #Delete the name of p2 object
print("Name is :",p2.name)