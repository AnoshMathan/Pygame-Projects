import pygame
import random

class Ship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("img_7.png")
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 400

    def Left(self):
        self.rect.x = self.rect.x-0.55

    def Right(self):
        self.rect.x = self.rect.x+0.55

class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("img_8.png")
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(50,450)
        self.rect.y = 10

    def movedown(self):
        self.rect.y = self.rect.y + random.uniform(0.25,0.6)

        if self.rect.y >= 500:
            self.rect.y = 10
            self.rect.x = random.randint(50,450)

class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load("img_9.png")
        self.image = pygame.transform.scale(self.image, (30, 50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def moveup(self):
        self.rect.y = self.rect.y - random.uniform(0.25,0.6)

        if self.rect.y <= 0:
            self.kill()

pygame.init()
screen = pygame.display.set_mode((500,500))
win = pygame.image.load("img_5.png")
win = pygame.transform.scale(win, (500, 500))
lose = pygame.image.load("img_6.png")
lose = pygame.transform.scale(lose, (500, 500))
score = 0

ship = Ship()
shipgroup = pygame.sprite.Group()
shipgroup.add(ship)

meteor1 = Meteor()
meteor2 = Meteor()
meteor3 = Meteor()
meteor4 = Meteor()
metgroup = pygame.sprite.Group()
metgroup.add(meteor1)
metgroup.add(meteor2)
metgroup.add(meteor3)
metgroup.add(meteor4)

bulletgroup = pygame.sprite.Group()

left = False
right = False
shipkilled = False

while True:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            left = True
            right = False

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            right = True
            left = False

        elif event.type == pygame.KEYUP:
            left = False
            right = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if shipkilled == False:
                b = Bullet(ship.rect.x + 25, ship.rect.y)
                bulletgroup.add(b)



    if left == True:
        ship.Left()

    if right == True:
        ship.Right()

    for meteor in metgroup:
        meteor.movedown()

    if score >= 50:
        ship.kill()
        meteor1.kill()
        meteor2.kill()
        meteor3.kill()
        meteor4.kill()

        for b in bulletgroup:
            b.kill()

        screen.blit(win,(0,0))
        pygame.display.update()
        pygame.time.delay(500)
        quit()


    lst = pygame.sprite.spritecollide(ship, metgroup, False)



    if len(lst) > 0:
        ship.kill()
        meteor1.kill()
        meteor2.kill()
        meteor3.kill()
        meteor4.kill()

        for b in bulletgroup:
            b.kill()

        screen.blit(lose, (0, 0))
        pygame.display.update()
        pygame.time.delay(500)
        quit()
        shipkilled = True

    for b in bulletgroup:
        b.moveup()
        lst = pygame.sprite.spritecollide(b, metgroup, False)

        if len(lst) > 0:
            b.kill()
            score = score + 1


        for val in lst:
            val.rect.y = 10
            val.rect.x = random.randint(50,450)

    shipgroup.draw(screen)
    metgroup.draw(screen)
    bulletgroup.draw(screen)
    pygame.display.update()
