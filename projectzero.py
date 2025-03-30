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
        k=0
    def update(self):
        global k
        keys = key.get_pressed()
       
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < 650:
            self.rect.x += self.speed
        
            final_sprite.rect.x-=self.speed
        if keys[K_SPACE] and self.on_ground:
            self.y_speed = -17
            self.on_ground = False
        if k==0:
            self.y_speed += 1 
            self.rect.y += self.y_speed
        
        if self.rect.y >= 400:
            self.rect.y = 400
            self.y_speed = 0
            self.on_ground = True

        if sprite.spritecollide(PlayerX1, benches_g, False):
            k=1
            PlayerX1.rect.y = 350
            PlayerX1.rect.y -= PlayerX1.speed
        else:
            k=0
k=0
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
        
class Birds(GameSprite):
    direction = "down"
    def update(self,a,b):
        if self.rect.y <= a:
            self.direction = "up"
            self.image=transform.scale(image.load(bird_image_u), (70, 50))
        if self.rect.y >= b:
            self.direction = "down"
            self.image=transform.scale(image.load(bird_image_d), (70, 50))
        if self.direction == "down":
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed

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
final_sprite=GameSprite("menu.png",20520,175,300,300,0)

bird_image_u = "Bird_u.png"
bird_image_d = "Bird_d.png"
Bird1 = Birds("bird_d.png", 400,100,30,20,8)
Bird2 = Birds("bird_d.png", 1000,100,30,20,8)
Bird3 = Birds("bird_d.png", 3500,100,30,20,8)
Bird4 = Birds("bird_d.png", 6000,100,30,20,8)
Bird5 = Birds("bird_d.png", 7200,100,30,20,8)
Bird6 = Birds("bird_d.png", 9000,100,30,20,8)
Bird7 = Birds("bird_d.png", 11200,100,30,20,8)
Bird8 = Birds("bird_d.png", 12000,100,30,20,8)
Bird9 = Birds("bird_d.png", 14000,100,30,20,8)

bench = "Bench.png"
bench1 = GameSprite("bench.png", 200,400,130,110,8)
bench2 = GameSprite("bench.png", 6000,400,130,110,8)
bench3 = GameSprite("bench.png", 11000,400,130,110,8)
benches_g = sprite.Group()
benches_g.add(bench1)
benches_g.add(bench2)
benches_g.add(bench3)

bin = "Bin.png"
bin1 = GameSprite("bin.png", 1100,420,100,80,8)
bin2 = GameSprite("bin.png", 2800,420,100,80,8)
bin3 = GameSprite("bin.png", 13000,420,100,80,8)
bins_g = sprite.Group()
bins_g.add(bin1)
bins_g.add(bin2)
bins_g.add(bin3)

donut = "donut.png"
donut1 = GameSprite("donut.png", 300,290,100,100,8)
donut2 = GameSprite("donut.png", 6100,290,100,100,8)
donut3 = GameSprite("donut.png", 11100,290,100,100,8)
donut4 = GameSprite("donut.png", 13000,290,100,100,8)
donuts_g = sprite.Group()
donuts_g.add(donut1)
donuts_g.add(donut2)
donuts_g.add(donut3)
donuts_g.add(donut4)



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
all_sprites.add(Bird1)
all_sprites.add(Bird2)
all_sprites.add(Bird3)
all_sprites.add(Bird4)
all_sprites.add(Bird5)
all_sprites.add(Bird6)
all_sprites.add(Bird7)
all_sprites.add(Bird8)
all_sprites.add(Bird9)
all_sprites.add(bench1)
all_sprites.add(bench2)
all_sprites.add(bench3)
all_sprites.add(bin1)
all_sprites.add(bin2)
all_sprites.add(bin3)
all_sprites.add(donut1)
all_sprites.add(donut2)
all_sprites.add(donut3)
all_sprites.add(donut4)
                                
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
        
        Bird1.update(100,450)
        Bird2.update(100,450)
        Bird3.update(100,450)
        Bird4.update(100,450)
        Bird5.update(100,450)
        Bird6.update(100,450)
        Bird7.update(100,450)
        Bird8.update(100,450)
        Bird9.update(100,450)

        bench1.update(450,700)
        bench2.update(450,700)
        bench3.update(450,700)

        bin1.update(450,700)
        bin2.update(450,700)
        bin3.update(450,700)

        donut1.update(450,700)
        donut2.update(450,700)
        donut3.update(450,700)
        donut4.update(450,700)

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
        window.blit(donut_score, (10,10))
        if local_shift != 0:
            window.blit(background, (local_shift - 800, 0)) 
            window.blit(donut_score, (10,10))

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

        if sprite.collide_rect(PlayerX1, Bird1):
            finish = True
            window.blit(proigrish, (100,200))
        if sprite.collide_rect(PlayerX1, Bird2):
            finish = True
            window.blit(proigrish, (100,200))
        if sprite.collide_rect(PlayerX1, Bird3):
            finish = True
            window.blit(proigrish, (100,200))
        if sprite.collide_rect(PlayerX1, Bird4):
            finish = True
            window.blit(proigrish, (100,200))
        if sprite.collide_rect(PlayerX1, Bird5):
            finish = True
            window.blit(proigrish, (100,200))
        if sprite.collide_rect(PlayerX1, Bird6):
            finish = True
            window.blit(proigrish, (100,200))
        if sprite.collide_rect(PlayerX1, Bird7):
            finish = True
            window.blit(proigrish, (100,200))
        if sprite.collide_rect(PlayerX1, Bird8):
            finish = True
            window.blit(proigrish, (100,200))
        if sprite.collide_rect(PlayerX1, Bird9):
            finish = True
            window.blit(proigrish, (100,200))
         for d in donuts:
            if sprite.collide_rect(PlayerX1, d):
                donuts.remove(d)
                d.kill()
                score_d = score_d + 1
                donut_score = font2.render('Пончики:' +str(score_d), True, (255, 255, 255))
                window.blit(donut_score, (10,10))

        if sprite.spritecollide(PlayerX1, benches_g, False):
            k=1
            PlayerX1.rect.y = 350
            PlayerX1.rect.y -= PlayerX1.speed
        else:
            k=0

        
        if sprite.spritecollide(PlayerX1, bins_g, False):
            k=1
            PlayerX1.rect.y = 350
            PlayerX1.rect.y -= PlayerX1.speed
        else:
            k=0

        
        if sprite.collide_rect(PlayerX1, final_sprite):
            finish = True
            window.blit(pobeda, (50,200))
        
        print(final_sprite.rect.x)
        
    display.update()
