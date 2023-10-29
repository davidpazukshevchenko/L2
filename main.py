class Student:
    def __init__(self,name ="Vasya",age =18):
        self.name = name
        self.age = age

    def say_hi(self):
        print(f"Hello my name is {self.name} and I am {self.age} old!")


first_student = Student("Petya",16)
second_student = Student("Anna",21)
third_student = Student()


first_student.say_hi()
second_student.say_hi()
third_student.say_hi()