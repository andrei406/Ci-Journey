from objetos import *
from pygame.constants import KEYDOWN, K_BACKSPACE, K_SPACE, K_a, K_d, K_q, K_w, QUIT
from os import path, putenv
import pygame
from pygame import locals
import os
from time import sleep

fase3 = pygame.mixer.Sound(os.path.join(diretorio_m, 'fase3.wav'))
fase3.set_volume(1)

fase3.play()

n_colisoes = 0

fim = pygame.mixer.Sound(os.path.join(diretorio_m, 'Game_over.wav'))
fim.set_volume(1)
cor_tela = (0 , 0, 255)

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

espinhos = Espinhos()
todasSprites.add(espinhos)
grupo_sprite2.add(espinhos)


for c in range(largura*2//64):
    chao = Chao(c)
    todasSprites.add(chao)

lua = Lua()
todasSprites.add(lua)

inimigo = Inimigos()
todasSprites.add(inimigo)
grupo_sprite2.add(inimigo)

arqueiro = Arqueiro()
todasSprites.add(arqueiro)
grupo_sprite2.add(arqueiro)

ci = Ci()
todasSprites.add(ci)

colidiu = False
espinhoOk = False
soldadoOk = False

colidir = False