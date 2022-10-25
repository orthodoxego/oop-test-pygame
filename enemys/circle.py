import pygame
from setup import *


class Circle:

    def __init__(self, x, y, color, diametr, width):
        self.x = x
        self.y = y
        self.color = color
        self.diametr = diametr
        self.width = width

        # Существует ли круг?
        self.enabled = True

        # Смещение по X и Y
        self.speed_x = 10
        self.speed_y = 10

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

        if self.x < 0 or self.x > WIDTH:
            self.speed_x *= -1

        if self.y < 0 or self.y > HEIGHT:
            self.speed_y *= -1


    def draw(self, scene):
        # Ctrl+Q
        pygame.draw.circle(scene, self.color, (self.x, self.y), self.diametr, self.width)