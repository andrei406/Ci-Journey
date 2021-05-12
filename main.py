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

            if not soldadoOk:
                soldado = Soldado()
                todasSprites.add(soldado)
                grupo_sprite2.add(soldado)
                soldado.movimentar()
                soldadoOk = True
        

        if chao.voltas == 2:
            inimigo.movimentar()
        
        if chao.voltas == 47:
            inimigo.denovo()
            espinhos.denovo()
            arbusto.denovo()
            arvore.denovo()

        arqueiro.movimentar()
        chao.movimentar()
        arbusto.movimentar()
        arvore.movimentar()
        if chao.voltas == 4:
            inimigo.voltas == chao.voltas
        
        if inimigo.velocidade >= 25:
            colidir = True
            espinhos.movimentar()
            espinhos.voltas == chao.voltas

    if colisoes and colidiu == False and colidir == True:
        colidiu = False
    if colidiu:
        chao.denovo()
        arbusto.denovo()
        arvore.denovo()
        inimigo.denovo()
        inimigo.ficalonge()
        if soldadoOk:
            soldado.ficalonge()
            soldado.denovo()
        espinhos.ficalonge()
        espinhos.denovo()
        fase3.stop()
        sleep(0.2)
        fim.play()
        sleep(4)
        fase2.play()
        colidiu = False
    todasSprites.draw(tela)
    todasSprites.update()
    pygame.display.flip()
"""
if chao.voltasCompletas == 2:
            inimigo.rect.y = altura + 50
            espinhos.rect.y = altura + 50
            soldado.rect.y = altura + 50
            if arbusto.voltas == 4:
                arbusto.rect.y = altura + 50
            if arvore.voltas == 5:
                arvore.rect.y = altura + 50
        
        if chao.voltasCompletas == 2:
            
"""