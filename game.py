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
rc = randint(0, 255)
gc = randint(0, 255)
bc = randint(0, 255)
image = pygame.image.load(os.path.join(path, '2.jpg'))
imh, imw = image.get_rect().size

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx = -1
                if event.key == pygame.K_RIGHT:
                    dx = 1
                if event.key == pygame.K_UP:
                    dy = -1
                if event.key == pygame.K_DOWN:
                    dy = 1

    x += 0.04 * dx
    y += 0.04 * dy
    
    screen.fill((255, 255, 255))
    screen.blit(image, (x, y))
    # pygame.draw.circle(screen, (rc, gc, bc), (int(x), int(y)), r)

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
    pygame.display.flip()