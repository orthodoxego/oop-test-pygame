import pygame
from setup import *
from enemys.circle import Circle

pygame.init()
pygame.display.set_caption("Test OOP")
size = [WIDTH, HEIGHT]
scene = pygame.display.set_mode(size)
clock = pygame.time.Clock()
playGame = True
deltatime = 0

crc = Circle(WIDTH // 2, HEIGHT // 2, (255, 0, 0), 20, 2)

while playGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playGame = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                playGame = False

    scene.fill((0, 0, 0))

    # ============================================

    crc.move()
    crc.draw(scene)

    # ============================================
    pygame.display.flip()
    deltatime = clock.tick(FPS) / 1000


