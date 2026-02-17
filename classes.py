class Person:
    def __init__(self,name ,age,email):
        self.name = name
        self.age = age
        self.email = email


person1 = Person("Alice",20,"alice@gmail.com")
print(type(person1))
print(person1.name)
print(person1.age)
print(person1.email)