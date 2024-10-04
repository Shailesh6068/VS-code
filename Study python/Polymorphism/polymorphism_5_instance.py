class person:
    age = 50

    def fun(self,age1):
        self.age = age1


p1 = person()
p1.fun(60)
print(p1.age)
print(person.age)