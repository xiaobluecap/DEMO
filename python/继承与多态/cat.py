from animal import Animal

class Cat(Animal):
    def __init__(self,animal):
        # super(Cat,self).__init__(animal)
        Animal.__init__(self,animal)
