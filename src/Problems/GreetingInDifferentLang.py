from abc import ABC, abstractmethod
class Greeting():
    @abstractmethod
    def greet(self):
        pass

class EnglishGreeting(Greeting):
    def __init__(self):
        self.grtStr = "Hi"
    def greet(self):
        return self.grtStr

class SpanishGreeting(Greeting):
    def __init__(self):
        self.grtStr = "Hola"
    def greet(self):
        return self.grtStr
class HindiGreeting(Greeting):
    def __init__(self):
        self.grtStr = "Namaskar"
    def greet(self):
        return self.grtStr

greetings = [EnglishGreeting(), SpanishGreeting(), HindiGreeting()]
for grting in greetings:
    print( grting.greet(), end=",")

