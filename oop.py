class students:
    def __init__(self,name,gender,age):
        self.name=name
        self.gender=gender
        self.age=age
    def sayhello(self):
        print("my name is ",self.name,"i am",self.gender)

#creating objects
myobj= students("kavavu","male",30)
