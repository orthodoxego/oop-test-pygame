import pygame
from random import randint
 
class Square:

    def __init__(self, x, y, color, r, d, e, i):
        self.x = x
        self.y = y
        self.color = color
        self.r = r
        self.d = d
        self.e = e
        self.i = i

    def move(self):
        self.x += randint(0, 5)
        self.y += randint(0, 5)

    def resize(self):
        self.r += randint(0, 3)
        self.d += randint(0, 3)
        self.i += randint(0, 1)

    def draw(self, scene):
        pygame.draw.rect(scene, self.color, (self.x, self.y, self.r, self.d), self.e)
        pygame.draw.circle(scene, self.color, (self.x + 100, self.y + 100), self.i)
        pygame.draw.circle(scene, (254, 235, 167), (self.x + 40, self.y + 20), self.i)
        pygame.draw.circle(scene, (0, 0, 0), (self.x + 40, self.y + 20), self.i, 3)
    
