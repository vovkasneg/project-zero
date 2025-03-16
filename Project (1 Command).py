from pygame import *
from random import randint

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, x, y, speed):
        super().__init__(x, y, speed)
        self.y_speed = 0 
        self.on_ground = False
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < 650:
            self.rect.x += self.speed
        if keys[K_SPACE] and self.on_ground:
            self.y_speed = -15
            self.on_ground = False
        self.y_speed += 1 
        self.rect.y += self.y_speed
        if self.rect.y >= 400:
            self.rect.y = 400
            self.y_speed = 0
            self.on_ground = True

class Enemy(GameSprite):
    direction = "left"
    def update(self):
        if self.rect.x <= 450:
            self.direction = "right"
        if self.rect.x >= 600:
            self.direction = "left"
        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
class Button():
    def __init__(self, color, x, y, w, h, text, fsize, txt_color):

        self.width = w
        self.height = h
        self.color = color

        self.image = Surface([self.width, self.height])
        self.image.fill((color))
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.fsize = fsize
        self.text = text
        self.txt_color = txt_color
        self.txt_image = font.Font('font/impact.ttf', fsize).render(text, True, txt_color)

    def draw(self, shift_x, shift_y): # цей метод малює кнопку із тектом в середині. Сам текст зміщенний на величини shift_x та shift_y
        win.blit(self.image, (self.rect.x, self.rect.y))
        win.blit(self.txt_image, (self.rect.x + shift_x, self.rect.y + shift_y))
window = display.set_mode((800,600))
display.set_caption("Project Zero")
background = transform.scale(image.load("background.png"),(800,600))
font.init()
font = font.SysFont(None, 80)
pobeda = font.render('Ви виграли, дякуємо за гру!', True, (255, 255, 255))
proigrish = font.render('Нажаль, ви не змогли пройти гру...', True, (180, 0, 0))

PlayerX1 = Player("Player.png", 200,400,200,200,30)
#Enemy1 = Enemy("Enemy1.png", randint(80,600), randint(-100,0), 50, 50, randint(1,6))
game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background, (0,0))
        PlayerX1.reset()
        PlayerX1.update()

        #if sprite.spritecollide(PlayerX1, Enemy1, False):
            #finish = True
            #window.blit(proigrish, (200,200))
    display.update()
