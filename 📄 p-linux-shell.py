import pygame
import random

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

fog = pygame.Surface((1280, 720))
fog.set_alpha(40)

running = True
while running:
    clock.tick(60)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

    screen.fill((40, 40, 40))

    for _ in range(150):
        x = random.randint(0, 1280)
        y = random.randint(0, 720)
        pygame.draw.circle(fog, (180,180,180), (x,y), 20)

    screen.blit(fog, (0,0))
    pygame.display.flip()