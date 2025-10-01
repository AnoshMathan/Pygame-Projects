import pygame
import random

class Basket(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("img_2.png")
        self.image = pygame.transform.scale(self.image, (100, 80))
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 400

    def Left(self):
        self.rect.x = self.rect.x-25

    def Right(self):
        self.rect.x = self.rect.x+25


class Apple(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("img_3.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(50,450)
        self.rect.y = 10


    def movedown(self):
        self.rect.y = self.rect.y + random.uniform(0.25,0.6)

        if self.rect.y >= 500:
            self.rect.y = 10
            self.rect.x = random.randint(50,450)

class Rotapple(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("img_4.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(50,450)
        self.rect.y = 10


    def Rmovedown(self):
        self.rect.y = self.rect.y + random.uniform(0.4, 0.6)

        if self.rect.y >= 500:
            self.rect.y = 10
            self.rect.x = random.randint(50,450)

pygame.init()
screen = pygame.display.set_mode((500,500))

bas = Basket()
basgroup = pygame.sprite.Group()
basgroup.add(bas)


app1 = Apple()
app2 = Apple()
app3 = Apple()
app4 = Apple()
appgroup = pygame.sprite.Group()
appgroup.add(app1)
appgroup.add(app2)
appgroup.add(app3)
appgroup.add(app4)

Rotapp1 = Rotapple()
Rotgroup = pygame.sprite.Group()
Rotgroup.add(Rotapp1)


score = 0
font = pygame.font.Font('freesansbold.ttf', 32)

win = pygame.image.load("img_5.png")
lose = pygame.image.load("img_6.png")
win = pygame.transform.scale(win, (500,500))
lose = pygame.transform.scale(lose, (500,500))

while True:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            bas.Left()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            bas.Right()

    lst = pygame.sprite.spritecollide(bas, appgroup, False)
    lst2 = pygame.sprite.spritecollide(bas, Rotgroup, False)

    for val in lst:
        score = score + 5
        val.rect.y = 10
        val.rect.x = random.randint(50, 450)

    for val in lst2:
        score = score - 5
        val.rect.y = 10
        val.rect.x = random.randint(50, 450)

    text = font.render('Score: ' + str(score), True, (0, 0, 0), (255, 255, 255))
    textRect = text.get_rect()
    textRect.center = (400, 20)
    screen.blit(text, textRect)

    if score >= 0 and score < 50:
        for apple in appgroup:
            apple.movedown()

        for Rotapple in Rotgroup:
            Rotapple.Rmovedown()

    else:

        for apple in appgroup:
            apple.kill()

        for apple in Rotgroup:
            Rotapple.kill()

    if score >= 50:
        screen.blit(win,(0,0))

    if score < 0:
        screen.blit(lose, (0,0))

    appgroup.draw(screen)
    basgroup.draw(screen)
    Rotgroup.draw(screen)
    pygame.display.update()