'''
class P(object):
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    # def __repr__(self):
    #      return '-----%s'%self.name

class S(P):
    def __init__(self,name,age,gender):
         P.__init__(self,name,age,gender)
        # super(S,self).__init__()

    def __repr__(self):
        return '--%s'%self.name

s=S('tomas',20,1)
print(s)


class Person(object):
      def __init__(self,name,sex):
          self.name = name
          self.sex = sex

      def print_title(self):
          if self.sex == "male":
              print("man")
          elif self.sex == "female":
             print("woman")

class Child(Person):                # Child 继承 Person
     def print_title(self):
         if self.sex == "male":
             print("boy")
         elif self.sex == "female":
             print("girl")

May = Child("May","female")
Peter = Person("Peter","male")

print(May.name,May.sex,Peter.name,Peter.sex)
May.print_title()
Peter.print_title()

'''


class Person(object):
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex

    def print_title(self):
        if self.sex == "male":
            print("man")
        elif self.sex == "female":
            print("woman")


class Child(Person):
    pass


class Baby(Child):
    pass


May = Baby("May", "female")  # 继承上上层父类的属性
print(May.name, May.sex)
May.print_title()  # 可使用上上层父类的方法


class Child(Person):
    def print_title(self):
        if self.sex == "male":
            print("boy")
        elif self.sex == "female":
            print("girl")


class Baby(Child):
    pass


May = Baby("May", "female")
May.print_title()  # 优先使用上层类的方法