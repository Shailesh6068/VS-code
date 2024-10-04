#public access specifier
class Access:
    def __init__(self):
        self.a = 5
        print("It is public")
        
    def public(self, name):
        self.m = 5
        self.q = name
        print(f"The value of m is {self.m} and name is {name} ")     # here is naem is accessed.

a1 = Access()  # Corrected instantiation
# print(a1.m)  # This will raise an error, as 'm' is not yet initialized
a1.public("raj")  # Calling public() method
print(a1.m)    # Now you can access 'm' after calling the 'public()' method
print(a1.q)