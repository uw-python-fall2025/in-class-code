
class Pet:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self):
        return f'Pet {self.name} is {self.color} '

    def speak(self):
        print(f'The pet {self.name} says something.')

    def get_name(self):
        return f'Pet: {self.name}'

class Dog(Pet):
    def __init__(self, name, color):
        super().__init__(name, color)

    def speak(self):
        print(f'The dog {self.name} says Arf!')

class Cat(Pet):
    def __init__(self, name, color):
        super().__init__(name, color)

    def __str__(self):
        return f'Cat {self.name} hates Mondays'

    def speak(self):
        print(f'The cat {self.name} says Meow')


snoopy = Dog('Snoopy', 'white')
garfield = Cat('Garfield', 'orange')

print(snoopy)
print(garfield)

snoopy.speak()
garfield.speak()
