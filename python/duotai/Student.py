from Person import Person

class Student(Person):
    def __init__(self,name):
        Person.__init__(self,name)
    def SayMyWork(self):
        print(self.name+' is a student,for learn')