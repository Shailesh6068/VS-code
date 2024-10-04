class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print(f"The name is {name} and age is {age}.")

student1 = student("Ram",45)
student1.eng_marks = 46
print(student1.eng_marks)


        