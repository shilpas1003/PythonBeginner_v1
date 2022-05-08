class Animal:
    def __init__(self):
        print("Animal is Here")

    def sound(self):
        print("Animal Sounds")


# Define class Dog
class Dog(Animal):
    def __init__(self, name, breed):
        # super().__init__()
        self.name = name
        self.breed = breed

    def getname(self):
        return self.name

    def getbreed(self):
        return self.breed

    def sound(self):
        print("Dog Barks")

# Define class Cat
class Cat(Animal):

        def __init__(self, name, breed):
            # super().__init__()
            self.name = name
            self.breed = breed

        def getname(self):
            return self.name

        def getbreed(self):
            return self.breed

        def sound(self):
            print("Cat Meows")

def main():
    print("Main call")
    A1 = Animal()
    A1.sound()
    A2 = Animal()
    D1 = Dog("Bolt", "Doberman")
    D1.sound()
    C1 = Cat("Robin", "Persian")
    C1.sound()

main()