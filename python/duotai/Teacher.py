from Person import Person

class Teacher(Person):
    def __init__(self,name):
        Person.__init__(self,name)
    def SayMyWork(self):
        print(self.name+' is a teacher,for teacher student')