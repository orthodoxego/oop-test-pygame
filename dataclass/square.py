import pygame
from random import randint
 
class Square:

    def __init__(self, x, y, color, r, d, e):
        self.x = x
        self.y = y
        self.color = color
        self.r = r
        self.d = d
        self.e = e

    def move(self):
        self.x += randint(-5, 5)
        self.y += randint(-5, 5)

    def resize(self):
        self.r += randint(0, 1024)
        self.d += randint(0, 768)

    def draw(self, scene):
        pygame.draw.rect(scene, self.color, (self.x, self.y, self.r, self.d), self.e)
    
