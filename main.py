import pygame
from pygame import locals
import os

from pygame.constants import QUIT

diretorio_p = os.path.dirname(__file__)
diretorio_i = os.path.join(diretorio_p, 'imagens')

pygame.init()

altura = 480
largura = 640

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Ci Journey')

imagem_fundo = pygame.image.load(os.path.join(diretorio_i, 'cenario-basico.png')).convert()
imagem_fundo = pygame.transform.scale(imagem_fundo, (largura,altura))

relogio = pygame.time.Clock()
while True:
    relogio.tick(30)
    tela.blit(imagem_fundo, (0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
