from os import path
import pygame
from pygame import locals
import os
from time import sleep

from pygame.constants import KEYDOWN, K_BACKSPACE, K_SPACE, K_q, K_w, QUIT

diretorio_p = os.path.dirname(__file__)
diretorio_i = os.path.join(diretorio_p, 'imagens')
diretorio_m = os.path.join(diretorio_p, 'musicas')

pygame.init()

altura = 480
largura = 640

pygame.mixer.init()
musica_intro = pygame.mixer.Sound(os.path.join(diretorio_m, 'intro.wav'))
musica_intro.set_volume(.7)
musica_intro.play(-1)

fase1 = pygame.mixer.Sound(os.path.join(diretorio_m, 'fase1.wav'))
fase1.set_volume(1)
select = pygame.mixer.Sound(os.path.join(diretorio_m, 'selec.wav'))
select.set_volume(1)

cor_tela = (0, 255, 255)
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Ci Journey')
a = 2

"""
Imagem de fundo retirada

imagem_fundo = pygame.image.load(os.path.join(diretorio_i, 'cenario-basico.png')).convert()
imagem_fundo = pygame.transform.scale(imagem_fundo, (largura,altura))
"""
ci_shet = pygame.image.load(os.path.join(diretorio_i, 'ci-princes-sprites.png')).convert_alpha()
cenario_shet = pygame.image.load(os.path.join(diretorio_i, 'cenario-sprites.png'))
class Ci(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.siga = self.volte = self.pule = False
        self.ci_img = []
        for i in range(2):
            img = ci_shet.subsurface((i * 32, 0), (32, 32))
            img = pygame.transform.scale(img, (32* 2, 32 * 2))
            self.ci_img.append(img)
        self.index_lista = 0
        self.image = self.ci_img[self.index_lista]
        self.rect = self.image.get_rect()
        self.rect.center = (50, altura-70)
    def vai(self):
        self.siga = True
    def update(self):
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
        self.rect.y = altura - 450
#class Arvore(pygame.sprite.Sprite):
#class Arbusto(pygame.sprite.Sprite):

start = False
todasSprites = pygame.sprite.Group()

for c in range(largura*2//64):
    chao = Chao(c)
    todasSprites.add(chao)
sol = Sol()
todasSprites.add(sol)
ci = Ci()
todasSprites.add(ci)

relogio = pygame.time.Clock()
while True:
    relogio.tick(30)
    tela.fill(cor_tela)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                if start == False:
                    select.play()
                    musica_intro.set_volume(0)
                    del musica_intro
                    start = True
                    sleep(3)
                    tela.fill((0,0,0))
                    sleep(5)
                    fase1.play()
                else:
                    pass
            
            if event.key == K_w:
                ci.vai()
            if event.key == K_q:
                pygame.quit()
                exit()       
                    
    todasSprites.draw(tela)
    todasSprites.update()
    pygame.display.flip()
