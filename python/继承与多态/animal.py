class Animal(object):
    def __init__(self,animal):
        self.animal=animal
    def eat(self):
        print(self.animal + " eat food")