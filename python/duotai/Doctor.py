from Person import Person
class Doctor(Person):
    def __init__(self,name):
        Person.__init__(self,name)
    def SayMyWork(self):
        print(self.name+' is a doctor,for Heal the sick')