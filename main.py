from os import path
import pygame
from pygame import locals
import os
from time import sleep
from configuracoes import *
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
                    musica_intro.set_volume(0)
                    del musica_intro
                    select.play()
                    start = True
                    sleep(5)
                    tela.fill((0,0,0))
                    fase1.play()
                else:
                    pass
            if start:
                chao.movimentar()
                arbusto.movimentar()
                arvore.movimentar()
                inimigo.movimentar()
            if event.key == K_w:
                ci.pular()
            if event.key == K_q:
                pygame.quit()
                exit()                          
    todasSprites.draw(tela)
    todasSprites.update()
    pygame.display.flip()