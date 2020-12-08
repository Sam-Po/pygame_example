import pygame
import os
from random import randint

path = os.path.dirname(os.path.realpath(__file__))

pygame.init()
screen = pygame.display.set_mode([500, 500])
run = True
x = 150
y = 50
r = 20
dx = 1
dy = 1
pad_x = 200
pad_dx = 0
image = pygame.image.load(os.path.join(path, 'tennis.png'))
imh, imw = image.get_rect().size

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    pad_dx = -0.04
                if event.key == pygame.K_RIGHT:
                    pad_dx = 0.04
    pad_x += pad_dx
    if pad_x > 500 - 80 or pad_x < 0:
        pad_dx = 0

    x += 0.03 * dx
    y += 0.03 * dy

    screen.fill((255, 255, 255))
    screen.blit(image, (x, y))
    pygame.draw.rect(screen, (0, 0, 0), [pad_x, 450, 80, 10])


    if x > (500 - imh) or x < 0:
        rc = randint(0, 255)
        gc = randint(0, 255)
        bc = randint(0, 255)
        dx *= -1
    if y > (500 - imw) or y < 0:
        rc = randint(0, 255)
        gc = randint(0, 255)
        bc = randint(0, 255)
        dy *= -1
    if (x + imw / 2) > pad_x and (x + imw / 2) < (pad_x + 80)\
        and (y + imh) > 450 and (y + imh) < 452:
        dy *= -1
    pygame.display.flip()