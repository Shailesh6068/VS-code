# class fun:
#     i = 0
#     k = 0

#     def load():
#         print("i :",i)
#         i = i+1
# f1 = fun()
# f1.load()
# print("k :",f1.k)

class fun:
    i = 0
    k = 0

    def load(self):  # You need to pass 'self' as the first parameter in methods
        print("i :", self.i)  # Access class variable with 'self'
        self.i = self.i + 1  # Access and modify class variable with 'self'

    def load1(self):
        print(self.i)
        
f1 = fun()
f1.load()
f1.load1()
print("k :", f1.k)
