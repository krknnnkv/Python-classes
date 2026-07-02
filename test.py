class Pet:
    count: int = 0
    def __init__(self, name:str, color:str):
        self.name = name
        self.color = color
        Pet.count += 1

    def __del__(self):
        Pet.count -= 1

    def voice(self):
        print()

    def call(self, name:str):
        if self.name == name:
            self.voice()

class Cat(Pet):
    count: int = 0
    def voice(self):
        print("meow")
    def __init__(self, name:str, color:str):
        super().__init__(name, color)
        Cat.count += 1

    def __del__(self):
        super().__del__()
        Cat.count -= 1


class Dog(Pet):
    count: int = 0
    def voice(self):
        print("bark")

    def __init__(self, name:str, color:str):
        super().__init__(name, color)
        Dog.count += 1

    def __del__(self):
        super().__del__()
        Dog.count -= 1

murzik = Cat("Murzik", "red")
barbos = Dog("Barbos", "black")
barsik = Dog("Barsik", "grey")
marsik = Cat("Marsik", "grey")

murzik.call(murzik.name)
Cat.call(murzik, murzik.name)
print(Pet.count)
#del barsik
print(Pet.count)
print(Cat.count)
print(Dog.count)


#инкапсуляция, наследование, полиморфизм
