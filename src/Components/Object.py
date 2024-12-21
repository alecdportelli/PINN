import numpy as np

from Utils.Integration import RK4


class Object:
    def __init__(self, mass):
        self.mass = mass
        self.CoG = np.array([0, 0, 0])

        self.x = 0
        self.y = 0
        self.z = 0

        self.xVelo = 0
        self.yVelo = 0

        self.xAccel = 0
        self.yAccel = 0

        self.thrust = np.array([0, 0, 0])


    def SetThrust(self, magnitude):
        self.thrust = np.array([magnitude, 0, 0])


    def UpdateDynamics(self, dt):
        RK4(self, dt)  
    

class Sphere(Object):
    def __init__(self, radius, mass=1):
        super().__init__(mass)
        self.radius = radius
        self.cD = 0.47
        self.cA = np.pi * (self.radius**2)

    
class Cylinder(Object):
    def __init__(self, radius, length, mass=1):
        super().__init__(mass)
        self.radius = radius
        self.length = length
        self.cD = 1.2
        self.cA = 2 * self.radius * self.length


class Cube(Object):
    def __init__(self, length, mass=1):
        super().__init__(mass)
        self.length = length
        self.cD = 1.05
        self.cA = self.length**2


class EquilTriangle(Object):
    def __init__(self, base, height, mass=1):
        super().__init__(mass)
        self.base = base
        self.height = height
        self.cD = 1.05
        self.cA = self.base * self.height * (0.5)
