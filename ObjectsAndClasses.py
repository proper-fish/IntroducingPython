class Thing():
    pass

# class attribute
class Thing2():
    letters = 'abc'

# object attribute
class Thing3():
    def __init__(self):
        self.letters = 'xyz'

# open attributes
class Element():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
    def __str__(self):
        return ('name: %s symbol: %s number: %s' % (self.name, self.symbol, self.number))

# hidden attributes
class HiddenElement():
    def __init__(self, name, symbol, number):
        self.__name = name
        self.__symbol = symbol
        self.__number = number
    @property
    def name(self):
        return self.__name
    @property
    def symbol(self):
        return self.__symbol
    @property
    def number(self):
        return self.__number

# polymorphism
class Laser():
    def does(self):
        return 'disintegrate'

class Claw():
    def does(self):
        return 'crush'

class Smartphone():
    def does(self):
        return 'ring'

class Robot():
    def __init__(self):
        self.laser = Laser()
        self.claw = Claw()
        self.smartphone = Smartphone()
    def does(self):
        return ('A laser is to %s, a claw is to %s, a smartphone is to %s'
            % (self.laser.does(), self.claw.does(), self.smartphone.does()))