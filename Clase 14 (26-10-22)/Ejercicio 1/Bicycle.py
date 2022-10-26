from Vehicle import Vehicle

class Bicycle(Vehicle):
    def __init__(self, color, wheels, type):
        Vehicle.__init__(self, color, wheels)
        self.type = type

class Motorcycle(Bicycle):
    def __init__(self, color, wheels, type, speed, cc):
        Bicycle.__init__(self, color, wheels, type)
        self.speed = speed
        self.cc = cc
        