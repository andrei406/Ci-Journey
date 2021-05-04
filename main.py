from configuracoes import *
while True:
    relogio.tick(30)
    tela.fill(cor_tela)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_w:
                if not ci.pulo and ci.desce:
                    pass
                else:
                    ci.pular()
            if event.key == K_q:
                pygame.quit()
                exit()                          
    colisoes = pygame.sprite.spritecollide(ci, grupo_sprite2, False, pygame.sprite.collide_mask)
    if start:
        if chao.voltasCompletas == 1:
            if espinhoOk == False:
                espinhos = Espinhos()
                todasSprites.add(espinhos)
                espinhos.movimentar()
                espinhoOk = True
        if chao.voltasCompletas == 2:
            inimigo.rect.y = altura + 50
            espinhos.rect.y = altura + 50
            if arbusto.voltas == 4:
                arbusto.rect.y = altura + 50
            if arvore.voltas == 5:
                arvore.rect.y = altura + 50
        else:
            chao.movimentar()
            arbusto.movimentar()
            arvore.movimentar()
            inimigo.movimentar()
    if colisoes and colidiu == False:
        ...
        #colidiu = True
    if colidiu:
        chao.denovo()
        arbusto.denovo()
        arvore.denovo()
        inimigo.denovo()
        inimigo.ficalonge()
        fase2.stop()
        sleep(0.2)
        fim.play()
        sleep(4)
        fase2.play()
        colidiu = False
    todasSprites.draw(tela)
    todasSprites.update()
    pygame.display.flip()
