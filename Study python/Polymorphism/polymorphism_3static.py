#self method
class sample:
    def __init__(self):
        pass

    @staticmethod
    def fun(name,roll_no):
       return name ,roll_no

    def fun1(age):
        age1 = age
s1 =sample()
s1.a, s1.b = s1.fun("John", 123)
print("Name :", s1.a,"\n","Roll No. :", s1.b)
s1.fun1(23)