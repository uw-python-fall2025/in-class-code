
class Cat:
    def __init__(self, name, color):
        self.name = name
        self._color = color


class Dog:

    def __init__(self, name, color):
        self.name = name
        self._color = color
        self._age = 5

    def __str__(self):
        return f'{self.name} is {self.color} years old'

    def __repr__(self):
        return f'{self.name} is {self.color} years old'

    def speak(self):
        print(f'{self.name} the {self._color} dog says: Arf!!')

    @property
    def color(self):
        print('Getting the color')
        return self._color

    @color.setter
    def color(self, new_color):
        print('Updating the color')
        self._color = new_color

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        if new_age < 0 or new_age > 20:
            raise ValueError('Invalid age')
        self._age = new_age

dubs = Dog('Dubs', 'gray')
snoopy = Dog('Snoopy', 'white')

print(dubs)

# dubs.speak()
# snoopy.speak()
#
# print('Dubs color is ' + dubs.color)
# dubs.color = 'purple'
#
# dubs.speak()
#
# dubs.age = -6
#
# { 'name': "", 'color': "" }
#
