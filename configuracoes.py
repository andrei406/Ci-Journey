from objetos import *
from pygame.constants import KEYDOWN, K_BACKSPACE, K_SPACE, K_a, K_d, K_q, K_w, QUIT
from os import path, putenv
import pygame
from pygame import locals
import os
from time import sleep

fase2 = pygame.mixer.Sound(os.path.join(diretorio_m, 'fase2.wav'))
fase2.set_volume(1)

fase2.play()

n_colisoes = 0

fim = pygame.mixer.Sound(os.path.join(diretorio_m, 'Game_over.wav'))
fim.set_volume(1)
cor_tela = (0, 255, 255)

a = 2
pulou = False

start = True
todasSprites = pygame.sprite.Group()
grupo_sprite2 = pygame.sprite.Group()

relogio = pygame.time.Clock()
arvore = Arvore()
todasSprites.add(arvore)

"""espinhos = Espinhos()
todasSprites.add(espinhos)"""

arbusto = Arbusto()
todasSprites.add(arbusto)


for c in range(largura*2//64):
    chao = Chao(c)
    todasSprites.add(chao)

sol = Sol()
todasSprites.add(sol)

inimigo = Inimigos()
todasSprites.add(inimigo)
grupo_sprite2.add(inimigo)



ci = Ci()
todasSprites.add(ci)

colidiu = False
espinhoOk = False