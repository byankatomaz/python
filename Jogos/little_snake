import pygame
from random import randint
from pygame.locals import *
from sys import exit


class Game_Snake:

    def __init__(self):

        self.RED = 255, 0, 0
        self.GREEN = 0, 255, 0
        self.WHITE = 255, 255, 255
        self.BLACK = 0, 0, 0

        self.width = 700
        self.height = 1000

        self.point = 0
        self.compSnake = 5
        self.SPEED = 20

        self.X_SNAKE = int(self.width/2)
        self.Y_SNAKE = int(self.height/2)

        self.X_SCON = self.SPEED
        self.Y_SCON = 0

        self.W_SNAKE = 20
        self.H_SNAKE = 20

        self.X_APPLE = randint(60, 640)
        self.Y_APPLE = randint(60, 900)

        self.W_APPLE = 20
        self.H_APPLE = 20

        self.gameover = False

        self.clock = pygame.time.Clock()

        self.listSnake = []

        self.windowP = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Little Snake')

    def window(self):

        pygame.init()
        self.running()

    def running(self):
        while True:

            self.clock.tick(20)

            self.songs()

            self.windowP.fill(self.WHITE)
            self.restrict()
            self.interaction()
            self.apple()
            self.snake()
            self.collision()
            self.points()

            if self.gameover:
                self.gameOver()

            pygame.display.update()

    def snake(self):
        self.snakeP = pygame.draw.rect(self.windowP, self.GREEN, (self.X_SNAKE, self.Y_SNAKE, self.W_SNAKE, self.H_SNAKE))

    def apple(self):
        self.appleP = pygame.draw.rect(self.windowP, self.RED, (self.X_APPLE, self.Y_APPLE, self.W_APPLE, self.H_APPLE))

    def interaction(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    if self.X_SCON == -self.SPEED:
                        continue
                    else:
                        self.X_SCON = self.SPEED
                        self.Y_SCON = 0

                elif event.key == K_LEFT:
                    if self.X_SCON == self.SPEED:
                        continue
                    else:
                        self.X_SCON = -self.SPEED
                        self.Y_SCON = 0

                elif event.key == K_UP:
                    if self.Y_SCON == self.SPEED:
                        continue
                    else:
                        self.Y_SCON = -self.SPEED
                        self.X_SCON = 0

                elif event.key == K_DOWN:
                    if self.Y_SCON == -self.SPEED:
                        continue
                    else:
                        self.Y_SCON = self.SPEED
                        self.X_SCON = 0

        self.X_SNAKE += self.X_SCON
        self.Y_SNAKE += self.Y_SCON

    def collision(self):

        if self.snakeP.colliderect(self.appleP):
            self.X_APPLE = randint(60, 640)
            self.Y_APPLE = randint(60, 900)
            self.point += 1

            self.song_coin.play()
            self.compSnake += 1

        self.listHead = []
        self.listHead.append(self.X_SNAKE)
        self.listHead.append(self.Y_SNAKE)

        self.listSnake.append(self.listHead)

        if self.listSnake.count(self.listHead) > 1:
            self.gameOver()

        if len(self.listSnake) > self.compSnake:
            del self.listSnake[0]

        self.increasing_body(self.listSnake)

    def increasing_body(self, listSnake):

        for XeY in listSnake:
            pygame.draw.rect(self.windowP, self.GREEN, (XeY[0], XeY[1], self.W_SNAKE, self.H_SNAKE))

    def points(self):

        self.textPoint = pygame.font.SysFont('arial', 40, True, True)

        self.message = f'Points: {self.point}'
        self.exiText = self.textPoint.render(self.message, True, self.BLACK)

        self.windowP.blit(self.exiText, (480, 50))

    def gameOver(self):

        self.textTwo = pygame.font.SysFont('arial', 20, True, True)
        self.messageTwo = 'Game over! Pressione a tecla R para jogar novamente'
        self.exiTextTwo = self.textTwo.render(self.messageTwo, True, (0, 0, 0))
        self.textRect = self.exiTextTwo.get_rect()

        self.gameover = True

        while self.gameover:
            self.windowP.fill(self.WHITE)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()

                if event.type == KEYDOWN:
                    if event.key == K_r:
                        self.returnGame()

            self.textRect.center = (self.width // 2, self.height // 2)
            self.windowP.blit(self.exiTextTwo, self.textRect)
            pygame.display.update()

    def returnGame(self):

            self.point = 0
            self.compSnake = 5

            self.X_SNAKE = self.width / 2
            self.Y_SNAKE = self.height / 2

            self.X_APPLE = randint(60, 640)
            self.Y_APPLE = randint(60, 900)

            self.listHead = []
            self.listSnake = []

            self.gameover = False

    def restrict(self):

        if self.X_SNAKE > self.width:
            self.X_SNAKE = 0
        if self.X_SNAKE < 0:
            self.X_SNAKE = self.width
        if self.Y_SNAKE < 0:
            self.Y_SNAKE = self.height
        if self.Y_SNAKE > self.height:
            self.Y_SNAKE = 0


    def songs(self):

        pygame.mixer.music.set_volume(0.2)
        self.song_background = pygame.mixer.music.load('song_background.mp3')
        pygame.mixer.music.play(-1)

        self.song_coin = pygame.mixer.Sound('smw_coin.wav')


game = Game_Snake()
game.window()
