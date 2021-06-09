class Student():
    def __init__(self,name,age):
        self.name = name
        self.age = age

John = Student('John','23')

Jane = Student('Jane','22')

print(getattr(John,'age','25'))

print(getattr(John,'age'))
