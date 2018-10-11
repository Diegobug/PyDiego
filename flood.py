import pygame
import random

#função de flood
def flood(cor_atual,matriz,i,j,nova_cor):
    if(nova_cor == cor_atual or cor_atual!= matriz[i][j]):
        return
    elif(0<=i<6 and 0<=j<6):
        matriz[i][j] = nova_cor
        flood(cor_atual,matriz,i+1,j,nova_cor)# direita
        flood(cor_atual,matriz,i,j+1,nova_cor)# baixo
        flood(cor_atual,matriz,i,j-1,nova_cor)# esquerda
        flood(cor_atual,matriz,i-1,j,nova_cor)# cima
        
pygame.init()
#criando as cores  
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
#configurando a tela
screen = pygame.display.set_mode((640,480))
pygame.display.set_caption("flood")
screen.fill(white)
#criando a matriz
matriz = [[0 for x in range(7)] for y in range(7)]
#criando um vetor de cores
vetorCores = [black,red,green,blue]
#texto
jogada = 0
fonte = pygame.font.SysFont("Comic Sams MS", 30)
texto = fonte.render("Jogada "+str(jogada),False,(0,0,0))
#preenche a matriz com numeros aleatorios
for i in range(6):
    for j in range(6):
        matriz[i][j] = random.randint(0,3)
print(matriz)

controle = True
while controle:
    screen.fill(white)
    for evento in pygame.event.get():
        if(evento.type == pygame.QUIT):
            controle = False
        for i in range(6):
            for j in range(6):
                rect = (i*50,j*50,50,50)
                pygame.draw.rect(screen,vetorCores[matriz[i][j]],rect,0)

        if (evento.type == pygame.MOUSEBUTTONUP):
            x, y = pygame.mouse.get_pos() 
            flood(matriz[0][0],matriz,0,0,matriz[x//50][y//50])
            jogada = jogada+1
            texto = fonte.render("Jogada "+str(jogada),False,(0,0,0))

        screen.blit(texto,(0,310))
        pygame.display.update()            
pygame.quit() 






