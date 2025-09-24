import pygame
import random

class Floor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("img_11.png")
        self.image = pygame.transform.scale(self.image, (500, 100))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 400

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("img_14.png")
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(50,450)
        self.rect.y = random.randint(180,200)

class Mario(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("img_13.png")
        self.image = pygame.transform.scale(self.image, (40, 60))
        self.rect = self.image.get_rect()
        self.rect.x = 250
        self.rect.y = 340
        self.vely = 0
        self.on_ground = True
        self.mask = pygame.mask.from_surface(self.image)

    def left(self):
        self.image = pygame.image.load("img_13inv.png")
        self.image = pygame.transform.scale(self.image, (40, 60))
        self.rect.x -= 5

    def right(self):
        self.image = pygame.image.load("img_13.png")
        self.image = pygame.transform.scale(self.image, (40, 60))
        self.rect.x += 5

    def jump(self):
        if self.on_ground:   # jump only if standing
            self.vely = -15
            self.on_ground = False

    def update(self):
        # apply gravity
        self.vely += 1
        self.rect.y += self.vely

        # floor collision (y = 400 is top of floor image)
        if self.rect.bottom >= 400:
            self.rect.bottom = 400
            self.vely = 0
            self.on_ground = True

    def die(self):
        self.rect.y = self.rect.y + 3
        self.on_ground = False

        if self.rect.y > 500:
            self.kill()



class Goomba(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("img_15.png")
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.x = 800
        self.rect.y = 353
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        self.rect.x = self.rect.x - 1
        if self.rect.x < 0:
            self.rect.x = 1000

class Bomb(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("img_17.png")
        self.image = pygame.transform.scale(self.image, (45, 60))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(50, 450)
        self.rect.y = -150
        self.mask = pygame.mask.from_surface(self.image)

    def fall(self):
        self.rect.y = self.rect.y + 2
        if self.rect.y > 550:
            self.rect.y = 0
            self.rect.x = random.randint(50, 450)


pygame.init()
screen = pygame.display.set_mode((500,500))
font = pygame.font.Font('freesansbold.ttf', 32)
left = False
right = False
score = 0
dead = False

music = False
pygame.mixer.music.load('mariomusic.mp3')
if music == True:
    pygame.mixer.music.play(-1)


floor = Floor()
floorgroup = pygame.sprite.Group(floor)

mario = Mario()
mariogroup = pygame.sprite.Group(mario)

coingroup = pygame.sprite.Group(Coin(), Coin(), Coin())

goomba = Goomba()
goombagroup = pygame.sprite.Group(goomba)

bomb = Bomb()
bombgroup = pygame.sprite.Group(bomb)


bg = pygame.image.load("img_12.png")
bg = pygame.transform.scale(bg, (500,400))

ground = pygame.image.load("img_11.png")
ground = pygame.transform.scale(ground, (500, 100))

clock = pygame.time.Clock()

lose_image = pygame.image.load("img_16.png")
lose_image = pygame.transform.scale(lose_image, (400, 300))

next_level = pygame.image.load("img_18.png")
next_level = pygame.transform.scale(next_level, (200, 200))
nextlevel = False


start = True
startlevel = pygame.image.load("img_20.png")
startlevel = pygame.transform.scale(startlevel, (200, 100))

temp = True

while True:
    if start == True:
        screen.blit(startlevel, (160, 200))
        pygame.display.update()
        pygame.time.delay(3000)
        start = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); quit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_a and dead == False:
            left = True
            right = False

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_d and dead == False:
            right = True
            left = False

        elif event.type == pygame.KEYUP:
            left = False
            right = False

        elif event.type == pygame.KEYDOWN and event.key in (pygame.K_w, pygame.K_SPACE):
            mario.jump()

    lst = pygame.sprite.spritecollide(mario, coingroup, False)
    lst2 = pygame.sprite.spritecollide(mario, goombagroup, False, pygame.sprite.collide_mask)
    lst3 = pygame.sprite.spritecollide(mario, bombgroup, False, pygame.sprite.collide_mask)

    for val in lst:
        if nextlevel == True:
            score = score + 10
        else:
            score = score + 5

        val.rect.x = random.randint(50, 450)
        val.rect.y = random.randint(180, 200)

    if len(lst2) > 0 or len(lst3) > 0:
        dead = True



    goomba.move()

    if score >= 50 and nextlevel == False:
        screen.blit(next_level, (200, 100))
        pygame.display.update()
        pygame.time.delay(2000)
        nextlevel = True


    if nextlevel == True:
        bomb.fall()


    text = font.render('Score: ' + str(score), True, (0, 0, 0), (255, 255, 255))
    textRect = text.get_rect()
    textRect.center = (400, 20)

    if dead == True:
        mario.die()

        if temp == True:
            pygame.mixer.music.load('super-mario-death-sound-sound-effect.mp3')
            pygame.mixer.music.play(1)
            temp = False

    if left == True:
        mario.left()

    if right == True:
        mario.right()

    screen.blit(bg, (0,0))
    screen.blit(text, textRect)

    floorgroup.draw(screen)
    coingroup.draw(screen)

    if dead == False:
        mariogroup.update()

    if dead == False:
        goombagroup.draw(screen)
        bombgroup.draw(screen)

    mariogroup.draw(screen)

    if mario.rect.y > 500:
        screen.blit(lose_image, (50, 100))

    pygame.display.update()

    clock.tick(60)