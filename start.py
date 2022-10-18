import pygame
from setup import *
from random import randint
from dataclass.circle import Circle

pygame.init()
pygame.display.set_caption("Test OOP")
size = [WIDTH, HEIGHT]
scene = pygame.display.set_mode(size)
clock = pygame.time.Clock()
playGame = True
deltatime = 0

crc = []
for i in range(10000):
    crc.append(Circle(randint(0, WIDTH), randint(0, HEIGHT),
                      (randint(0, 255), randint(0, 255), randint(0, 255)),
                      randint(5, 50)))

while playGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playGame = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                playGame = False

    scene.fill((0, 0, 0))
    # ============================================

    for i in range(len(crc)):
        crc[i].move()
        crc[i].draw(scene)

    # ============================================
    pygame.display.flip()


    deltatime = clock.tick(FPS) / 1000