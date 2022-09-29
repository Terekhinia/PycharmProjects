"""def output(self, a):
    print(a)

class Class_name:
    x = 1
    y = 1
    func = output
    def __init__(self, nev_x, nev_y):
        self.x = nev_x
        self.y = nev_y

x = Class_name(10, 10)
x.func(100)"""





"""class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay


    def last_name(self):
        return self.name.split()[1]


    def give_raise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    def __str__(self):
        return '[Person: ' + self.name + ', '+ str(self.pay) + ']'

class Manager(Person):
    def __init__(self, name, pay):
        Person.__init__(self, name, 'mgr', pay)

    def give_raise(self, percent, bonus=100):
        Person.give_raise(self, percent + bonus)


ivan = Person('Ivan Petrov')
John = Person('John Sidorov', job='dev', pay=100000)

John.give_raise(.10)
print(ivan.last_name())
print(John)"""


"""class Dog:
    
    def __init__(self, name, voices=None):
        self.name = name
        self.voices = voices

    def voice(self, voices):
        self.voices = voices
        return self.voices


    def __str__(self):
        return 'Название животного: ' + self.name + ', '+ self.voices

dog = Dog('Собакен')
dog.voice('gaf')
print(dog)


class Cat(Dog):
    def __init__(self, name, voices=None):
        Dog.__init__(self, name, voices)

    def voice(self, q):
        q=q*2
        Dog.voice(self, q[:4] + '-' + q[:4])


cat = Cat('Котяра')
cat.voice('myau')
print(cat)

class Mouse(Dog):
    def __init__(self, name, voices=None):
        Dog.__init__(self, name, voices)

    def voice(self, q):
        Dog.voice(self, q[::-1])


mouse = Mouse('Мышь')
mouse.voice('ясьтедорк')
print(mouse)
"""


"""class Dog:
    num = 0
    def __init__(self, voices=None):

        self.voices = voices
        Dog.num = Dog.num + 1

    def voice(self, voices):
        self.voices = voices
        return self.voices

    def print_num():
        print(Dog.num)

    print_num = staticmethod(print_num)

    def __str__(self):
        return 'Название животного: ' + self.name + ', '+ self.voices

Dog.print_num()
a = Dog()
a.print_num()"""

class Animal:
    num = 0

    def voice(self, voice):
        self.voice = voice
        print(self.voice)
        Animal.num = Animal.num + 1

    def print_num():
            print(Animal.num)

    print_num = staticmethod(print_num)

class Dog(Animal):

    def voice(self, voices):
        Animal.voice(self, voices)
d = Dog()
d.voice('gaf')

class Cat(Animal):

    def voice(self, voices):
        Animal.voice(self, voices[:4] + '-' + voices[:4])
c = Cat()
c.voice('myu')

class Mouse(Animal):

    def voice(self, voices):
        Animal.voice(self, voices[::-1])
m = Mouse()
m.voice('ясьтедорк')
Animal.print_num()
