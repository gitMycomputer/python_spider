class Animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def run(self):
        print(self.name,"is running")
class dog:

    def __init__(self,na,age):
        pass
    def run(self):
        super(Animal, self).__init__(na, age)
        # super语句
a=Animal("a",18)
a.run()
# b=dog()
# c=0