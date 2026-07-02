#инкапсуляция
from asyncio import Protocol
from typing import List


class Phone:
    def __init__(self, name):
        self.name = name
        self._battery = 100

    def use(self, percent):
        if percent <= self._battery:
            self._battery -= percent
            print(f"{percent}% battery used")
        else:
            print("charge your phone")

    def charge(self):
        self._battery = 100
        print("battery is charged")

    def get_battery(self):
        return self._battery

phone = Phone("iphone")
phone.use(56)
print(phone.get_battery())
phone.charge()
print(phone.get_battery())
print()

#наследование

class Transport:
    def __init__(self, name):
        self.name = name

    def start(self):
        print(f"{self.name} engine is running")

class Car(Transport):
    def roll_window(self):
        print("ride with a breeze)")

class Bus(Transport):
    def open_the_doors(self):
        print("people are inside, you can go")

car =  Car("volkswagen")
car.start()
car.roll_window()

bus = Bus("Bus")
bus.start()
bus.open_the_doors()
print()

#полиморфизм

class Species(Protocol):
    def speak(self) -> None:
        ...

class Cat(Species):
    def speak(self):
        print("Meow")

class Dog(Species):
    def speak(self):
        print("Woof")

class Parrot(Species):
    def speak(self):
        print("Squawk")

animals: List[Species] = [Cat(), Dog(), Parrot()]
for animal in animals:
    animal.speak()