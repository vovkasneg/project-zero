from pygame import *
from random import randint
font.init()
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
    def __init__(self, x, y, speed, size_x, size_y, player_speed):
        super().__init__(x, y, speed, size_x, size_y, player_speed)
        self.y_speed = 0 
        self.on_ground = False
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < 650:
            self.rect.x += self.speed
        if keys[K_SPACE] and self.on_ground:
            self.y_speed = -17
            self.on_ground = False
        self.y_speed += 1 
        self.rect.y += self.y_speed
        if self.rect.y >= 340:
            self.rect.y = 340
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
        self.txt_image = font.Font(None, fsize).render(text, True, txt_color)
    
    def draw(self, shift_x, shift_y): # цей метод малює кнопку із тектом в середині. Сам текст зміщенний на величини shift_x та shift_y
        window.blit(self.image, (self.rect.x, self.rect.y))
        window.blit(self.txt_image, (self.rect.x + shift_x, self.rect.y + shift_y))

window = display.set_mode((800,600))
display.set_caption("Project Zero")
background = transform.scale(image.load("background.png"),(800,600))

font1 = font.SysFont(None, 80)
pobeda = font1.render('Ви виграли, дякуємо за гру!', True, (255, 255, 255))
proigrish = font1.render('Нажаль, ви не змогли пройти гру...', True, (180, 0, 0))

mixer.init()
main = mixer.Sound("main_music.ogg")


PlayerX1 = Player("Player.png", 50,400,160,160,10)
Enemy1 = Enemy("Enemy.png", randint(80,600), 330, 200, 200, randint(1,6))
game = False
finish = False


window=display.set_mode((800,600))
display.set_caption("Місія: школа")
background_m=transform.scale(image.load("menu.png"),(800,600))
btn_start = Button((107, 107, 107), 250, 100, 280, 70, 'START GAME', 50, (255, 255, 255))
btn_exit = Button((107, 107, 107), 250, 300, 280, 70, 'EXIT GAME', 50, (255, 255, 255))
btn_settings = Button((107, 107, 107), 250, 200, 280, 70, 'SETTINGS', 50, (255, 255, 255))

menu=True
# завантажуємо звуки
mixer.init()
main_m = mixer.Sound("menu_music.ogg")

while menu:
    for e in event.get():
        if e.type==QUIT:
            menu=False
    main_m.play()
    window.blit(background_m,(0,0))
    btn_start.draw(15,5)
    btn_settings.draw(15,5)
    btn_exit.draw(15,5)
    display.update()
    time.delay(50)
    pos_x, pos_y = mouse.get_pos()

    for e in event.get():
        if btn_start.rect.collidepoint((pos_x, pos_y)) and e.type == MOUSEBUTTONDOWN:
            menu=False
            game = True
            main_m.stop()
while game:
    main.play()
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background, (0,0))
        PlayerX1.reset()
        PlayerX1.update()
        Enemy1.reset()
        Enemy1.update()

        if sprite.collide_rect(PlayerX1, Enemy1):
            finish = True
            window.blit(proigrish, (200,200))
    display.update()
