#inheritance allows oop class to inherit attribute
#and methods from another class
class animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        pass
class dog(animal):
    def speak(self):
        return "woof"
class cat(animal):
    def speak(self):
        return "meow"
#this are objects
doggy=dog("buddy")
cat=cat("whisker")
print(doggy.speak())
print(cat.speak())

