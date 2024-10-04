class student:
    def __init__(self,name,age):
        self.name = name            #class attribute
        self.age = age
        print(f"The name is {name} and age is {age}.")

student1 = student("Ram",45)
student1.eng_marks = 46              #instance attribute
print(student1.eng_marks)