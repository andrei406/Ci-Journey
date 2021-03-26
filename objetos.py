from os import path
import pygame
from pygame import locals
import os
a = 2

altura = 640
largura = 1008
pygame.init()
pygame.mixer.init()

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Ci Journey')

diretorio_p = os.path.dirname(__file__)
diretorio_i = os.path.join(diretorio_p, 'imagens')
diretorio_m = os.path.join(diretorio_p, 'musicas')

ci_shet = pygame.image.load(os.path.join(diretorio_i, 'ci-princes-sprites.png')).convert_alpha()
cenario_shet = pygame.image.load(os.path.join(diretorio_i, 'cenario-sprites.png'))

class Ci(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.siga = self.volte = self.pule = self.desce = False
        self.ci_img = []
        self.pulo = False
        for i in range(2):
            img = ci_shet.subsurface((i * 32, 32), (32, 32))
            img = pygame.transform.scale(img, (32* 2, 32 * 2))
            self.ci_img.append(img)
        self.index_lista = 0
        self.image = self.ci_img[self.index_lista]
        self.rect = self.image.get_rect()
        self.rect.center = (50, altura-70) #(50, altura - 70)
    def vai(self):
        self.siga = True
    def volta(self):
        self.volte = True
    def pular(self):
        self.pulo = True
    def descer(self):
        self.desce = True
    def update(self):
        if self.pulo:
            if self.rect.y <=400:
                self.desce = True
                self.pulo = False
            else:
                self.rect.y -=20
                self.rect.x += 30
                '''if self.vai:
                    '''
                '''else:
                    self.rect.x -=10'''
        elif self.desce == True:
            if self.rect.y >= altura - 130:
                self.desce = False
            self.rect.y +=20
            self.rect.x += 30
        elif self.siga == True:
            if self.rect.x >= 940:
                self.siga = False
            else:
                self.rect.x += 20
        elif self.volte:
            if self.rect.x <= 10:
                pass
            else:
                self.rect.x -= 20
        else:
            if self.index_lista > 1:
                self.index_lista = 0
            self.index_lista += .10
            self.image = self.ci_img[int(self.index_lista)]
class Chao(pygame.sprite.Sprite):
    def __init__(self, pos_x):
        pygame.sprite.Sprite.__init__(self)
        self.image = cenario_shet.subsurface(((32 * 3) - 32, 0), (32, 32))
        self.image = pygame.transform.scale(self.image, (32*a, 32*a))
        self.rect = self.image.get_rect()
        self.rect.y = altura - 60
        self.rect.x = pos_x * 64
class Sol(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = cenario_shet.subsurface((32, 32), (32, 32))
        self.image = pygame.transform.scale(self.image, (32*3, 32*3))
        self.rect = self.image.get_rect()
        self.rect.x = largura - 90
        self.rect.y = altura - 620
class Arvore(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = cenario_shet.subsurface((0,64), (32,32))
        self.image = pygame.transform.scale(self.image, (32* 7, 32*7))
        self.rect = self.image.get_rect()
        self.rect.x = largura - 300
        self.rect.y = altura - 270
class Arbusto(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = cenario_shet.subsurface((32, 64), (32, 32))
        self.image = pygame.transform.scale(self.image, (32 * 5, 32 *5))
        self.rect = self.image.get_rect()
        self.rect.x = largura - 700
        self.rect.y = altura - 190
