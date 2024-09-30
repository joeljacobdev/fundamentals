from abc import ABC, abstractmethod


class ArtificialVoice:
    def produce_sound(self, text):
        pass


class Animal:
    def __init__(self, voice):
        self.voice = voice

    def speak(self):
        self.voice.produce_sound("I am an animal")


class Dog(Animal):
    def speak(self):
        self.voice.produce_sound("My name is doggo")


"""
Used to => Reuse and override behaviour (minor updates or add new behaviour)
"""


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)
