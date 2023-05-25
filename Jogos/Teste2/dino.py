import pygame
from pygame.locals import *
from sys import exit
from random import randrange
import os

WIDTH = 640
HEIGHT = 480


class Supreme:

    def __init__(self):
        self.directory_princ = os.path.dirname(__file__)
        self.images_directory = os.path.join(self.directory_princ, 'imagens')
        self.songs_directory = os.path.join(self.directory_princ, 'sons')

        self.sprite_sheet = pygame.image.load(os.path.join(self.images_directory, 'dinoSpritesheet.png')).convert_alpha()

        self.som_pulo = pygame.mixer.Sound(os.path.join(self.songs_directory, 'jump_sound.wav'))

class Chao(pygame.sprite.Sprite):
    def __init__(self, pos_x):
        pygame.sprite.Sprite.__init__(self)

        self.sprite_sheet = Supreme().sprite_sheet

        self.image = self.sprite_sheet.subsurface((6 * 32, 0), (32, 32))
        self.image = pygame.transform.scale(self.image, (32 * 2, 32 * 2))

        self.rect = self.image.get_rect()
        self.rect.y = HEIGHT - 92
        self.rect.x = pos_x * 64

    def update(self):
        if self.rect.topright[0] < 0:
            self.rect.x = WIDTH
        self.rect.x -= 10


class Dinossauro(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.supreme = Supreme()

        self.sprite_sheet = self.supreme.sprite_sheet
        self.supreme.som_pulo.set_volume(0.5)

        self.images_dino = []

        for i in range(3):
            img = self.sprite_sheet.subsurface((i * 32, 0), (32, 32))
            img = pygame.transform.scale(img, (32*3, 32*3))
            self.images_dino.append(img)

        self.index_lista = 0
        self.image = self.images_dino[self.index_lista]

        self.pos_y_inicial = 390 - 96 // 2
        self.rect = self.image.get_rect()
        self.rect.center = (100, self.pos_y_inicial)

        self.pulo = False

    def pular(self):
        self.pulo = True
        self.supreme.som_pulo.play()

    def update(self):

        if self.pulo:
            if self.rect.y <= 200:
                self.pulo = False
            self.rect.y -= 20
        else:
            if self.rect.y < self.pos_y_inicial:
                self.rect.y += 20

            else:
                self.rect.y = self.pos_y_inicial


        if self.index_lista > 2:
            self.index_lista = 0
        self.index_lista += 0.25

        self.image = self.images_dino[int(self.index_lista)]


class Nuvens(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.sprite_sheet = Supreme().sprite_sheet

        self.image = self.sprite_sheet.subsurface((7*32, 0), (32, 32))
        self.image = pygame.transform.scale(self.image, (32*3, 32*3))

        self.rect = self.image.get_rect()
        self.rect.y = randrange(50, 250, 50)
        self.rect.x = WIDTH - randrange(30, 300, 90)

    def update(self):

        if self.rect.topright[0] < 0:
            self.rect.x = WIDTH
            self.rect.y = randrange(50, 200, 50)

        self.rect.x -= 10


class Dino:
    def __init__(self):

        self.todas_as_sprites = pygame.sprite.Group()

        self.RED = 255, 0, 0
        self.GREEN = 0, 255, 0
        self.WHITE = 255, 255, 255
        self.BLACK = 0, 0, 0

        self.width = WIDTH
        self.height = HEIGHT

        self.pulo = False

        self.clock = pygame.time.Clock()

        self.windowP = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Dino')

    def window(self):

        pygame.init()
        pygame.mixer.init()

        self.dinossauro = Dinossauro()
        self.todas_as_sprites.add(self.dinossauro)

        for i in range(11):
            self.chao = Chao(i)
            self.todas_as_sprites.add(self.chao)

        for i in range(4):
            self.nuvem = Nuvens()
            self.todas_as_sprites.add(self.nuvem)

        self.running()

    def running(self):

        while True:

            self.clock.tick(30)

            self.windowP.fill(self.WHITE)
            self.interaction()
            self.drawing()

            pygame.display.flip()

    def interaction(self):

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    if self.dinossauro.rect.y != self.dinossauro.pos_y_inicial:
                        pass
                    else:
                        self.dinossauro.pular()

    #
    # def pulando(self):

    def drawing(self):

        self.todas_as_sprites.draw(self.windowP)
        self.todas_as_sprites.update()


game = Dino()
game.window()