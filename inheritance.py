# class Animal:
#     def __init__(self,name):
#         self.name = name
#         self.age = age

#     def make_sound(self):
#         print(f"{self.name} makes general sound")

# class Dog(Animal):
#     def make_sound(self):
#         print(f"{self.name} barks")
    

# class Horse(Animal):
#     def make_sound(self):
#         print(f"{self.name} neighs")


# a1 = Animal("jack")
# a1.make_sound()

# d1 = Dog("Max")
# print(d1.name)
# d1.make_sound()


# h1 = Horse("Tristan")
# print(h1.name)
# h1.make_sound()


class Person:
    def __init__(self,name,age):
        self.name= name
        self.age = age

    def works(self):
        print(f"{self.name} works")

    def display_info(self):
        print("------Person Details------")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


class Teacher(Person):
    def __init__(self, name, age,subject,salary):
        super().__init__(name, age)
        self.subject = subject
        self.salary = salary

    def works(self):
        print(f"{self.name} teaches")

    def display_info(self):
        super().display_info()
        print(f"Subject: {self.subject}")
        print(f"Salary: {self.salary}")


class Student(Person):
    def __init__(self, name, age,student_id,course):
        super().__init__(name, age)
        self.student_id = student_id
        self.course = course


    def works(self):
        print(f"{self.name} studies")

    def display_info(self):
        super().display_info()
        print(f"Subject: {self.student_id}")
        print(f"Salary: {self.course}")

#teacher object
t1 = Teacher("Joy",34,"Analytics",120000)
t1.works()
t1.display_info()


#student object
s1 = Student("Mark",20,"D112","Data Science")
s1.works()
s1.display_info()