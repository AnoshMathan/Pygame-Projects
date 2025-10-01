import pygame
pygame.init()

screen = pygame.display.set_mode((500,500))
screen.fill((255, 255, 255))
colour = (0,0,0)
rubber = pygame.image.load('img.png')
rubber = pygame.transform.scale(rubber,(50,50))
draw = False
rectangle = False
square = False
circle = False
line = False
start_pos=()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            (x, y) = pygame.mouse.get_pos()
            draw = True

            if rectangle == True or circle == True or square == True or line == True:
                draw = False
                start_pos=(x,y)

            elif x >= 10 and x <= 60 and y >= 10 and y <= 60:
                colour = (255, 0, 0)
            elif x >= 10 and x <= 60 and y >= 80 and y <= 130:
                colour = (0, 255, 0)
            elif x >= 10 and x <= 60 and y >= 150 and y <= 200:
                colour = (0, 0, 255)
            elif x >= 10 and x <= 60 and y >= 220 and y <= 270:
                colour = (255, 255, 0)
            elif x >= 10 and x <= 60 and y >= 290 and y <= 340:
                colour = (0, 255, 255)
            elif x >= 10 and x <= 60 and y >= 360 and y <= 410:
                colour = (255, 0, 255)
            elif x >= 10 and x <= 60 and y >= 420 and y <= 490:
                colour = (255, 255, 255)
            elif x >= 425 and x <= 475 and y >= 350 and y <= 450 and rectangle == False:
                draw = False
                rectangle = True
            elif x >= 425 and x <= 475 and y >= 270 and y <= 320 and square == False:
                draw = False
                square = True
            elif x >= 425 and x <= 475 and y >= 175 and y <= 225 and circle == False:
                draw = False
                circle = True
            elif x >= 450 and x <= 460 and y >= 100 and y <= 150 and line == False:
                draw = False
                line = True

        if event.type == pygame.MOUSEBUTTONUP:
            draw = False
            end_pos = pygame.mouse.get_pos()

            if rectangle == True and start_pos != ():

                if start_pos[0] < end_pos[0] and start_pos[1] > end_pos[1]:
                    pygame.draw.rect(screen, colour,pygame.Rect(start_pos[0], end_pos[1], abs(end_pos[0] - start_pos[0]),abs(end_pos[1] - start_pos[1])))

                elif start_pos[0] > end_pos[0] and start_pos[1] > end_pos[1]:
                    pygame.draw.rect(screen, colour,pygame.Rect(end_pos[0], end_pos[1], abs(end_pos[0] - start_pos[0]),abs(end_pos[1] - start_pos[1])))

                elif start_pos[0] > end_pos[0] and start_pos[1] < end_pos[1]:
                    pygame.draw.rect(screen, colour,pygame.Rect(end_pos[0], start_pos[1], abs(end_pos[0] - start_pos[0]),abs(end_pos[1] - start_pos[1])))

                else:
                    pygame.draw.rect(screen, colour, pygame.Rect(start_pos[0], start_pos[1], abs(end_pos[0]- start_pos[0]), abs(end_pos[1]- start_pos[1])))

                rectangle = False
                start_pos = ()
                end_pos = ()

            if square == True and start_pos != ():
                pygame.draw.rect(screen, colour, pygame.Rect(start_pos[0], start_pos[1], abs(end_pos[0] - start_pos[0]), abs(end_pos[0] - start_pos[0])))
                square = False
                start_pos = ()
                end_pos = ()

            if line == True and start_pos != ():
                pygame.draw.line(screen,colour, (start_pos[0], start_pos[1]), (end_pos[0], end_pos[1]), 10)
                line = False
                start_pos = ()
                end_pos = ()

            if circle == True and start_pos != ():
                pygame.draw.circle(screen, colour, (start_pos[0], start_pos[1]), abs(end_pos[0] - start_pos[0]), abs(end_pos[0] - start_pos[0]))
                circle = False
                start_pos = ()
                end_pos = ()

        if event.type == pygame.MOUSEMOTION and draw == True:
            pos = pygame.mouse.get_pos()
            pygame.draw.circle(screen, colour, pos, 10, 10)

    #colours
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(10, 10, 50, 50))
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(10, 80, 50, 50))
    pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(10, 150, 50, 50))
    pygame.draw.rect(screen, (255, 255, 0), pygame.Rect(10, 220, 50, 50))
    pygame.draw.rect(screen, (0, 255, 255), pygame.Rect(10, 290, 50, 50))
    pygame.draw.rect(screen, (255, 0, 255), pygame.Rect(10, 360, 50, 50))

    #shapes
    pygame.draw.line(screen, (0, 0, 0), (450, 100), (450, 150), 10)
    pygame.draw.circle(screen, (0, 0, 0), (450, 200), 25, 25)
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(425, 270, 50 ,50))
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(425, 350, 50, 100))
    screen.blit(rubber, (10, 420))

    pygame.display.update()