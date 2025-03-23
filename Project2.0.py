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
        
            final_sprite.rect.x-=self.speed
        if keys[K_SPACE] and self.on_ground:
            self.y_speed = -17
            self.on_ground = False
        self.y_speed += 1 
        self.rect.y += self.y_speed
        if self.rect.y >= 400:
            self.rect.y = 400
            self.y_speed = 0
            self.on_ground = True

class Enemy(GameSprite):
    direction = "left"
    def update(self,a,b):
        if self.rect.x <= a:
            self.direction = "right"
            self.image=transform.scale(image.load(enemy_image_r), (50, 100))
        if self.rect.x >= b:
            self.direction = "left"
            self.image=transform.scale(image.load(enemy_image_l), (50, 100))
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
background = transform.scale(image.load("background2.png"),(800,600))

font1 = font.SysFont(None, 80)
pobeda = font1.render('Ви виграли, дякуємо за гру!', True, (255, 255, 255))
proigrish = font1.render('Нажаль, ви не змогли пройти гру...', True, (180, 0, 0))

mixer.init()
main = mixer.Sound("main.music.ogg")

all_sprites = sprite.Group()

# список врагов:
enemies = sprite.Group()


PlayerX1 = Player("Player.png", 50,400,50,100,10)
enemy_image_l="Enemy_l.png"
enemy_image_r="Enemy_r.png"
Enemy1 = Enemy(enemy_image_l, 800, 400, 50, 100, randint(1,4))
Enemy2 = Enemy(enemy_image_l, 2000, 400, 50, 100, randint(1,4))
Enemy3 = Enemy(enemy_image_l, 5000, 400, 50, 100, randint(1,4))
Enemy4 = Enemy(enemy_image_l, 7000, 400, 50, 100, randint(1,4))
Enemy5 = Enemy(enemy_image_l, 8500, 400, 50, 100, randint(1,4))
Enemy6 = Enemy(enemy_image_l, 10000, 400, 50, 100, randint(1,4))
Enemy7 = Enemy(enemy_image_l, 11500, 400, 50, 100, randint(1,4))
Enemy8 = Enemy(enemy_image_l, 13000, 400, 50, 100, randint(1,4))
Enemy9 = Enemy(enemy_image_l, 14500, 400, 50, 100, randint(1,4))
final_sprite=GameSprite("menu.png",20000,200,300,300,0)

all_sprites.add(PlayerX1)
all_sprites.add(Enemy1)
all_sprites.add(Enemy2)
all_sprites.add(Enemy3)
all_sprites.add(Enemy4) 
all_sprites.add(Enemy5) 
all_sprites.add(Enemy6) 
all_sprites.add(Enemy7) 
all_sprites.add(Enemy8) 
all_sprites.add(Enemy9)  
                                
all_sprites.add(final_sprite)
game = False
finish = False

win_width = 800 
win_height = 600
left_bound = win_width / 20       # границы, за которые персонаж не выходит (начинает ехать фон)
right_bound = win_width - 8 * left_bound
shift = 0


window=display.set_mode((800,600))
display.set_caption("Місія: школа")
background_m=transform.scale(image.load("menu.png"),(800,600))
btn_start = Button((107, 107, 107), 250, 100, 280, 70, 'START GAME', 50, (255, 255, 255))
btn_exit = Button((107, 107, 107), 250, 300, 280, 70, 'EXIT GAME', 50, (255, 255, 255))
btn_settings = Button((107, 107, 107), 250, 200, 280, 70, 'SETTINGS', 50, (255, 255, 255))

menu=True
# завантажуємо звуки
mixer.init()
main_m = mixer.Sound("menu.music.ogg")

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
        
        Enemy1.update(450,700)
        Enemy2.update(450,700)
        Enemy3.update(450,700)
        Enemy4.update(450,700)
        Enemy5.update(450,700)
        Enemy6.update(450,700)
        Enemy7.update(450,700)
        Enemy8.update(450,700)
        Enemy9.update(450,700)

         # проверяем границы экрана: 
        if (
            PlayerX1.rect.x > right_bound and PlayerX1.speed > 0
            or
            PlayerX1.rect.x < left_bound and PlayerX1.speed < 0
        ): # при выходе влево или вправо переносим изменение в сдвиг экрана
            shift -= PlayerX1.speed  
            # перемещаем на общий сдвиг все спрайты (и отдельно предметов, они ж в другом списке):
            for s in all_sprites:
                s.rect.x -= PlayerX1.speed # сам PlayerX1 тоже в этом списке, поэтому его перемещение визуально отменится

        # Отрисовка
        # рисуем фон со сдвигом
        local_shift = shift % 800 
        window.blit(background, (local_shift, 0)) 
        if local_shift != 0:
            window.blit(background, (local_shift - 800, 0)) 

        # нарисуем все спрайты на экранной поверхности до проверки на выигрыш/проигрыш
        # если в этой итерации цикла игра закончилась, то новый фон отрисуется поверх персонажей
        all_sprites.draw(window)  
       

        if sprite.collide_rect(PlayerX1, Enemy1):
            finish = True
            window.blit(proigrish, (100,200))
        if sprite.collide_rect(PlayerX1, Enemy2):
            finish = True
            window.blit(proigrish, (100,200))
        if sprite.collide_rect(PlayerX1, Enemy3):
            finish = True
            window.blit(proigrish, (100,200))
        if sprite.collide_rect(PlayerX1, Enemy4):
            finish = True
            window.blit(proigrish, (100,200))
        if sprite.collide_rect(PlayerX1, Enemy5):
            finish = True
            window.blit(proigrish, (100,200))
        if sprite.collide_rect(PlayerX1, Enemy6):
            finish = True
            window.blit(proigrish, (100,200))
        if sprite.collide_rect(PlayerX1, Enemy7):
            finish = True
            window.blit(proigrish, (100,200))
        if sprite.collide_rect(PlayerX1, Enemy8):
            finish = True
            window.blit(proigrish, (100,200))
        if sprite.collide_rect(PlayerX1, Enemy9):
            finish = True
            window.blit(proigrish, (100,200))
        if sprite.collide_rect(PlayerX1, final_sprite):
            finish = True
            window.blit(pobeda, (50,200))
        print(final_sprite.rect.x)
        
    display.update()
