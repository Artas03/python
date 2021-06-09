class Student():
    class_="student"
    def __init__(self,name,age,mark1,mark2,mark3):
        self.name = name
        self.age = age
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3

    def calcAverage(self):
        return int(self.mark1 + self.mark2 + self.mark3)/3

Artas = Student("Artas","22", 89, 91, 67)
print(Artas.calcAverage())







