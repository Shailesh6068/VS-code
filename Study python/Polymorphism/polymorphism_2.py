class Animal:
    def speak():
        pass                # Placeholder for parent method
    
class dog(Animal):
    def speak(self):
        print("Bark.")
        
class cat(Animal):
    def speak(self):
        print("Meow")
        
class cow(Animal):
    def speak(self):
        print("Mooo")

a = dog()
c = cat()
co = cow()
a.speak()
c.speak()
co.speak()