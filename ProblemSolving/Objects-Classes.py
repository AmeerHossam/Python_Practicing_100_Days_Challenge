class Dog:

    # Simple Class
    # Attributes

    attr1 = "mammal"
    attr2 = "dog"
    
    #Behavior
    def fun(self):
        print(f"I am a {self.attr1}")
        print(f"I am a {self.attr2}")


class Subject:

    def __init__(self,attr1,attr2):
        self.attr1 = attr1
        self.attr2 = attr2
        print("Address of self:",id(self))

class Car:
    def __init__(self,model,color):
        self.model = model
        self.color = color

    def show(self):
        print(f"Model is {self.model} and the color is {self.color}")


audi = Car("Audi","White")
print(audi.show())
obj = Subject("Maths","Science")
print(obj.attr1, obj.attr2,id(obj))
new_obj = Subject("Maths","English")
print(id(new_obj))
#Object instantiation
Rodger = Dog()
Rodger.attr1 = "Not Mammal"
print(Rodger.attr1)
Rodger.fun()
