import pygame
from random import randint
class Circle:

    def __init__(self, x, y, color, diameter):
        self.x = x
        self.y = y
        self.color = color
        self.diameter = diameter

    def move(self):
        self.x += randint(-5, 5)
        self.y += randint(-5, 5)

    def draw(self, scene):
        pygame.draw.circle(scene, self.color, (self.x, self.y), self.diameter, 5)
