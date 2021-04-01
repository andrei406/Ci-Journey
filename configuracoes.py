from objetos import *

from pygame.constants import KEYDOWN, K_BACKSPACE, K_SPACE, K_a, K_d, K_q, K_w, QUIT

"""musica_intro = pygame.mixer.Sound(os.path.join(diretorio_m, 'intro.wav'))
musica_intro.set_volume(.5)
musica_intro.play(-1)"""

fase1 = pygame.mixer.Sound(os.path.join(diretorio_m, 'fase4.wav'))
fase1.set_volume(1)
select = pygame.mixer.Sound(os.path.join(diretorio_m, 'selec.wav'))
select.set_volume(1)
fase1.play()
cor_tela = (0, 0, 255)

a = 2

start = True
todasSprites = pygame.sprite.Group()
grupo_sprite2 = pygame.sprite.Group()

relogio = pygame.time.Clock()

for c in range(largura*2//64):
    chao = Chao(c)
    todasSprites.add(chao)

lua = Lua()
todasSprites.add(lua)

inimigo = Inimigos()
todasSprites.add(inimigo)
grupo_sprite2.add(inimigo)

arbusto = Arbusto()
todasSprites.add(arbusto)

arvore = Arvore()
todasSprites.add(arvore)

ci = Ci()
todasSprites.add(ci)

colidiu = False