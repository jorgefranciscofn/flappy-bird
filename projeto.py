import pygame 
import time 
import random


pygame.init()
## desenhar passaro  obs: tem de ser adicionado depois do fundo 
def desenhar(img,x,y):
    tela.blit(img,(x,y))
      
#informaçoes da tela
telaL=500
telaA=600
tela=pygame.display.set_mode((telaL,telaA))
pygame.display.set_caption('passaro')
#fundo
fundo=pygame.image.load('cenario.png')
fundo=pygame.transform.scale(fundo,(700,600))
#passaro 
pl=40
pa=20
px=50
py=350
pulo=0
passaro=pygame.image.load('passaro.png')
passaro=pygame.transform.scale(passaro, (pl, pa))
## canos
canolarg=60
canoy=random.randint(50,450) 
cano_cor=(0,128,0)
cano_movimento=-6
canox=500
clock=pygame.time.Clock()
rodar=True
##tela de fim 
fim_tela=pygame.image.load('fim.jpg')
fim_tela=pygame.transform.scale(fim_tela,(telaL,telaA))

##pontuação
pontos=0
fonte=pygame.font.Font('freesansbold.ttf',30) 
## função para desenhar o cano usando retangulos(rect)
def mostrar_cano(altura):
    pygame.draw.rect(tela,cano_cor,(canox,0,canolarg,altura))
    cano_baixo= 600 - altura -140
    pygame.draw.rect(tela,cano_cor,(canox,altura+140,canolarg,cano_baixo))
##Essa função ira calcular a colisão usando retangulos novamente mas dessa vez retangulos invisiveis que são atribuidos as entidades  
def colisao(canox, canoy, py, cano_baixo):
    cano_cima = pygame.Rect(canox, 0, canolarg, canoy)
    cano_baixo = pygame.Rect(canox, cano_baixo, canolarg, telaA - cano_baixo)
    passaro_rect = pygame.Rect(px, py, pl, pa)    
    return passaro_rect.colliderect(cano_cima) or passaro_rect.colliderect(cano_baixo)
##função para aparecer a pontuação
def mostrar_ponto(pontos):
    mostrar=fonte.render(f'{pontos}',True,(0,0,0))
    tela.blit(mostrar,(20,20))



while rodar:
    tela.blit(fundo,(0,0))
    clock.tick(30)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodar=False
        ## evento de pulo
        if event.type ==pygame.KEYDOWN:
            if event.key ==pygame.K_SPACE:
                pulo=-10 
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                pulo= 4   
    
    ##uso o evento de pulo para atualizar o y do passaro 
    py += pulo
    ##coloca limites na tela para o passaro 
    if py<=0:
        py=0
    if py>=580:
        py=580
    ##colocamos o x do cano com um numero especifico para que seu x diminua e ele se mova para a esquerda    
    canox +=cano_movimento
    ##gera novos canos 
    if canox <=-60:
        canox=500
        canoy=random.randint(50,450)
        pontos+=1
    ## mostra os canos     
    mostrar_cano(canoy)    
    cano_baixo = canoy + 140

    desenhar(passaro,px,py)
    mostrar_ponto(pontos)
    ## detectando a colizão o jogo ira mostrar a tela de game over e fecha apos 5 segunda
    if colisao(canox, canoy, py, cano_baixo):
        if colisao(canox, canoy, py, cano_baixo):
            tela.blit(fim_tela,(0,0))
            rodar=False
    
    pygame.display.update()   
time.sleep(5)
pygame.quit
