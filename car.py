import pygame

class Squar:
    def __init__(self, x, y, color, d, s):
        self.x = x
        self.y = y
        self.color = color
        self.d = d
        self.s = s

    def move(self):
        self.x -= 10

    def draw(self, scene):
        pygame.draw.rect(scene, self.color, (self.x, self.y, self.s, self.d))

class Circle:
    def __init__(self, x, y, color, diameter):
        self.x = x
        self.y = y
        self.color = color
        self.diameter = diameter

    def move(self):
        self.x -= 10

    def draw(self, scene):
        pygame.draw.circle(scene, self.color, (self.x, self.y), self.diameter)
