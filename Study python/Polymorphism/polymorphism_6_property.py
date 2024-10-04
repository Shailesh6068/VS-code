class property:

    def marks(self,math,phy,eng):
        self.math = math
        self.physics = phy
        self.english = eng

    @property                       #change the value due to  property decorator
    def percentge(self):
        return str((self.physics+self.math+self.english)/3)+"%"

p1 = property()
p1.marks(99,85,60)
print(p1.percentge)
p1.math = 90            # we change the value.
print(p1.percentge)     # print the changed the value.
