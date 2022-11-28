from Vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, color, wheels, speed, cc):
        Vehicle.__init__(self, color, wheels)
        self.speed = speed
        self.cc = cc
        

class Truck(Car):
    def __init__(self, color, wheels, speed, cc, charge):
        Car.__init__(self, color, wheels, speed, cc)
        self.charge = charge
        

    
