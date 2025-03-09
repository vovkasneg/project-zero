from pygame import *

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
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < 650:
            self.rect.y += self.speed
        if keys[K_SPACE]:
            self.rect.y -= 20

class Enemy(GameSprite):
    def __init__(self, x, y, speed):
        super().__init__(x, y, speed)
        self.direction = 1
    def update(self):
        self.rect.x += self.speed * self.direction
    if self.rect.x >= 800: 
        self.direction = -1  
    elif self.rect.x <= 0: 
        self.direction = 1

window = display.set_mode((800,600))
display.set_caption("Project Zero")
background = transform.scale(image.load("background.png"),(800,600))
