from pygame import *
from random import randint
from pygame import mixer
from PyQt5 import QtCore, QtWidgets

font.init()

# Создание основных классов игры
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

# Игрок
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

        if self.rect.y >= 400:
            self.rect.y = 400
            self.y_speed = 0
            self.on_ground = True

# Враги
class Enemy(GameSprite):
    direction = "left"
    def update(self, a, b):
        if self.rect.x <= a:
            self.direction = "right"
            self.image = transform.scale(image.load(enemy_image_r), (50, 100))
        if self.rect.x >= b:
            self.direction = "left"
            self.image = transform.scale(image.load(enemy_image_l), (50, 100))
        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

# Меню и интерфейс
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
    
    def draw(self, shift_x, shift_y):
        window.blit(self.image, (self.rect.x, self.rect.y))
        window.blit(self.txt_image, (self.rect.x + shift_x, self.rect.y + shift_y))

# Настройки интерфейса
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(210, 330, 151, 41))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 151, 41))
        self.label.setObjectName("label")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(10, 70, 121, 31))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(10, 110, 121, 31))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(10, 150, 121, 31))
        self.radioButton_3.setObjectName("radioButton_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 200, 131, 16))
        self.label_2.setObjectName("label_2")
        self.radioButton_4 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_4.setGeometry(QtCore.QRect(10, 230, 121, 31))
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_5 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_5.setGeometry(QtCore.QRect(10, 260, 121, 31))
        self.radioButton_5.setObjectName("radioButton_5")
        self.radioButton_6 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_6.setGeometry(QtCore.QRect(10, 290, 121, 31))
        self.radioButton_6.setObjectName("radioButton_6")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setGeometry(QtCore.QRect(390, 0, 194, 22))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Save Settings"))
        self.label.setText(_translate("MainWindow", "Налаштування Графіки"))
        self.radioButton.setText(_translate("MainWindow", "Низька"))
        self.radioButton_2.setText(_translate("MainWindow", "Середня"))
        self.radioButton_3.setText(_translate("MainWindow", "Висока"))
        self.label_2.setText(_translate("MainWindow", "Налаштування рівню"))
        self.radioButton_4.setText(_translate("MainWindow", "Простий"))
        self.radioButton_5.setText(_translate("MainWindow", "Середній"))
        self.radioButton_6.setText(_translate("MainWindow", "Високий"))

def settings():
    if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())

# Создание окна
window = display.set_mode((800, 600))
display.set_caption("Місія: школа")
background_m = transform.scale(image.load("menu.png"), (800, 600))

# Кнопки меню
btn_start = Button((107, 107, 107), 250, 100, 280, 70, 'START GAME', 50, (255, 255, 255))
btn_exit = Button((107, 107, 107), 250, 300, 280, 70, 'EXIT GAME', 50, (255, 255, 255))
btn_settings = Button((107, 107, 107), 250, 200, 280, 70, 'SETTINGS', 50, (255, 255, 255))

menu = True

mixer.init()
main_m = mixer.Sound("menu.music.ogg")

while menu:
    for e in event.get():
        if e.type == QUIT:
            menu = False
    main_m.play()
    window.blit(background_m, (0, 0))
    btn_start.draw(15, 5)
    btn_settings.draw(15, 5)
    btn_exit.draw(15, 5)
    display.update()
    time.delay(50)
    pos_x, pos_y = mouse.get_pos()

    for e in event.get():
        if btn_start.rect.collidepoint((pos_x, pos_y)) and e.type == MOUSEBUTTONDOWN:
            print("Start button clicked")
            # Настройки перед игрой или переход к новому экрану
            break
        if btn_exit.rect.collidepoint((pos_x, pos_y)) and e.type == MOUSEBUTTONDOWN:
            quit()
