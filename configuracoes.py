from objetos import *

from pygame.constants import KEYDOWN, K_BACKSPACE, K_SPACE, K_a, K_d, K_q, K_w, QUIT

musica_intro = pygame.mixer.Sound(os.path.join(diretorio_m, 'intro.wav'))
musica_intro.set_volume(.7)
musica_intro.play(-1)

fase1 = pygame.mixer.Sound(os.path.join(diretorio_m, 'fase1.wav'))
fase1.set_volume(1)
select = pygame.mixer.Sound(os.path.join(diretorio_m, 'selec.wav'))
select.set_volume(1)

cor_tela = (0, 255, 255)

a = 2

start = False
todasSprites = pygame.sprite.Group()

relogio = pygame.time.Clock()

for c in range(largura*2//64):
    chao = Chao(c)
    todasSprites.add(chao)

sol = Sol()
todasSprites.add(sol)

arbusto = Arbusto()
todasSprites.add(arbusto)

arvore = Arvore()
todasSprites.add(arvore)

ci = Ci()
todasSprites.add(ci)