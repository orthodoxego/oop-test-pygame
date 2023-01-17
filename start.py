import pygame
from setup import *
from random import randint
from car import *

p = 1
pygame.init()
pygame.display.set_caption("Test OOP")
size = [WIDTH, HEIGHT]
scene = pygame.display.set_mode(size)
clock = pygame.time.Clock()
playGame = True
deltatime = 0

car_3 = Squar(267, 356, (0, 176, 164), 120, 430)
car_2 = Squar(200, 428, (255, 0, 13), 120, 530)
car = Circle(300, 548, (50, 50, 50), 52)
car_1 = Circle(670, 548, (50, 50, 50), 52)

while playGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playGame = False
        elif event.type == pygame.K_UP:
            FPS += 5
        elif event.type == pygame.K_DOWN:
            FPS -= 5
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                playGame = False

    scene.fill((0, 0, 0))

    #car.move()
    car_3.draw(scene)
    car_2.draw(scene)
    car.draw(scene)
    car_1.draw(scene)
    car.move()
    car_1.move()
    car_2.move()
    car_3.move()

    pygame.display.flip()
    deltatime = clock.tick(FPS) / 1000
