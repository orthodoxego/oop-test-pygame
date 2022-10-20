import pygame
from random import randint
from setup import *

class Car:


    def __init__(self, x, y, color, n):
        self.x = x
        self.y = y
        self.color = color
        self.number = n

    def move(self):
        if (randint(0, 10) > 4):
            self.x += randint(1, 20)

        if (self.x > WIDTH):
            print(self.number)


    def draw(self, scene):
        pygame.draw.rect(scene, self.color, (self.x - 80, self.y - 50, 350, 60))
        pygame.draw.rect(scene, self.color, (self.x - 30, self.y - 100, 200, 50))
        pygame.draw.rect(scene, (200, 200, 255), (self.x - 25, self.y - 95, 190, 45))
        pygame.draw.circle(scene, (50, 50, 50), (self.x, self.y), 30)
        pygame.draw.circle(scene, (50, 50, 50), (self.x + 200, self.y), 30)

