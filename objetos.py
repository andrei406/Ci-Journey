from os import path
from time import sleep
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
inimigos_shet = pygame.image.load(os.path.join(diretorio_i, 'inimigos.png'))

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
        self.mask = pygame.mask.from_surface(self.image)
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
            if self.rect.y <=100:
                self.desce = True
                self.pulo = False
            else:
                self.rect.y -=45
        elif self.desce:
            if self.rect.y >= altura - 150:
                self.pulo = False   
                self.desce = False
            self.rect.y +=35
        elif self.siga:
            if self.rect.x >= 960:
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
        self.voltas = 0
        self.movimento = False
        self.velocidade = 10
        pygame.sprite.Sprite.__init__(self)
        self.image = cenario_shet.subsurface(((32 * 3) - 32, 0), (32, 32))
        self.image = pygame.transform.scale(self.image, (32*a, 32*a))
        self.rect = self.image.get_rect()
        self.rect.y = altura - 60
        self.rect.x = pos_x * 64
    def movimentar(self):
        self.movimento = True
    def maisRapido(self):
        self.velocidade += 10
    def menosRapido(self):
        self.velocidade -= 10
    def denovo(self):
        self.velocidade = 10
        self.voltas = 0
    def ficalonge(self):
        self.rect.x += 500
    def update(self):
        if self.movimento:
            if self.rect.topright[0] < 0:
                self.rect.x = largura + 200
                self.voltas += 1
                if self.velocidade < 30:
                    self.velocidade += 5
                elif self.voltas > 26:
                    if self.velocidade <= 50:
                        self.velocidade += 5
                    elif self.voltas == 120:
                        self.velocidade = 5
                    elif self.voltas == 135:
                        self.velocidade = 0
            self.rect.x -= self.velocidade
class Inimigos(Chao):
    def __init__(self):
        self.voltas = 0
        pygame.sprite.Sprite.__init__(self)
        self.velocidade = 10
        self.movimento = False
        self.inimigo_img = []
        self.pulo = False
        for i in range(2):
            img = inimigos_shet.subsurface((0, 32 * i),(32,32))
            img= pygame.transform.scale(img, (32* 4, 32 * 4))
            self.inimigo_img.append(img)
        self.index_lista = 0
        self.image = self.inimigo_img[self.index_lista]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.center = (1070, altura-120)
    def movimentar(self):
        self.movimento = True
class Sol(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = cenario_shet.subsurface((32, 32), (32, 32))
        self.image = pygame.transform.scale(self.image, (32*3, 32*3))
        self.rect = self.image.get_rect()
        self.rect.x = largura - 90
        self.rect.y = altura - 620
class Lua(Sol):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = cenario_shet.subsurface((64, 32), (32, 32))
        self.image = pygame.transform.scale(self.image, (32*3, 32*3))
        self.rect = self.image.get_rect()
        self.rect.x = largura - 90
        self.rect.y = altura - 620
class Arvore(Chao):
    def __init__(self):
        self.voltas = 0
        self.movimento = False
        self.velocidade = 10
        pygame.sprite.Sprite.__init__(self)
        self.image = cenario_shet.subsurface((0,64), (32,32))
        self.image = pygame.transform.scale(self.image, (32* 7, 32*7))
        self.rect = self.image.get_rect()
        self.rect.x = largura - 300
        self.rect.y = altura - 270
class Arbusto(Chao):
    def __init__(self):
        self.voltas = 0
        self.movimento = False
        self.velocidade = 10
        pygame.sprite.Sprite.__init__(self)
        self.image = cenario_shet.subsurface((32, 64), (32, 32))
        self.image = pygame.transform.scale(self.image, (32 * 5, 32 *5))
        self.rect = self.image.get_rect()
        self.rect.x = largura - 700
        self.rect.y = altura - 190
