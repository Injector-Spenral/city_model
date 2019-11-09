import math

class zone:
    def __init__(self, pos, ring):
        self.pos = pos # The position around the circle. 0 - 15
        self.ring = ring # The inner distance of the circle. 0 - city.radius
        self.area = math.pi * (2 * self.ring + 1) / 16

class city:
    def __init__(self, radius, population):
        self.radius = radius # Outer circle's inner radius
        self.population = population # Total population of city
        self.zones = [[zone(i, 0) for i in range(16)] for j in range(radius)]