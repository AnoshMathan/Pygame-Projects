import pygame
import random
pygame.init()

screen = pygame.display.set_mode((500,500))
screen.fill((255, 255, 255))
colour = (0,0,0)
x = 0
y = 0

while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            quit()
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            (x, y) = pygame.mouse.get_pos()
            colour = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            pygame.draw.circle(screen, colour, (x, y),40,40)


    pygame.display.update()