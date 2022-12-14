import pygame
from setup import *
from random import randint
from dataclass.circle import Circle
from dataclass.square import Square

pygame.init()
pygame.display.set_caption("Test OOP")
size = [WIDTH, HEIGHT]
scene = pygame.display.set_mode(size)
clock = pygame.time.Clock()
playGame = True
deltatime = 0

crc = []
for i in range(1):
    crc.append(Circle(randint(0, WIDTH), randint(0, HEIGHT),
                      (randint(0, 255), randint(0, 255), randint(0, 255)),
                      randint(5, 50)))

sqe = []
for i in range(100):
    x = randint(0, WIDTH)
    y = randint(0, HEIGHT)
    color = (randint(0, 255), randint(0, 255), randint(0, 255))
    r = randint(5, 50)
    d = randint(0, WIDTH)
    e = randint(0, HEIGHT)
    sqe.append(Square(x, y, color, r, d, e, i))

while playGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playGame = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                playGame = False

    scene.fill((0, 0, 0))

    # ============================================

    for i in range(len(sqe)):
        sqe[i].resize()
        sqe[i].move()
        sqe[i].draw(scene)

    # ============================================
    pygame.display.flip()


    deltatime = clock.tick(FPS) / 1000


