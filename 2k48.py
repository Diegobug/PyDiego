from random import randint
import pygame
import sys

matriz = [[0 for x in range(5)] for y in range(5)]

pygame.init()
#declaracao de variaveis
screen = pygame.display.set_mode((640,480))
pygame.display.set_caption("2k48")
font = pygame.font.SysFont("Courier New", 24)

def criarNumAleatorio():
    x1 = randint(0,4);x2 = randint(0,4)
    y1 = randint(0,4);y2 = randint(0,4)
    if(matriz[x1][y1]==0 and matriz[x2][y2]==0):
        matriz[x1][y1]=2
        matriz[x2][y2]=2
        for i in range(5):
            for j in range(5):
                numero = ""+str(matriz[i][j])
                text = font.render(numero, True, (255,0,0))
                screen.blit(text, (i*30,j*30))

    else:
        return criarNumAleatorio()
sair = True
criarNumAleatorio()

while(sair):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sair = False
             
    keys=pygame.key.get_pressed()
    
    
    if keys[pygame.K_LEFT]:
        criarNumAleatorio()
        for k in range(5):
            for i in range(5):
                for j in range(4):
                    if(matriz[i][j]==0):
                        matriz[i][j]=matriz[i][j+1]
                        matriz[i][j+1] = 0
                    elif(matriz[i][j]==matriz[i][j+1]):
                        matriz[i][j]+=matriz[i][j+1] 
                        matriz[i][j+1] = 0
    if keys[pygame.K_RIGHT]:
        criarNumAleatorio()
        for k in range(5):
            for i in range(5):
                for j in range(4):
                    if(matriz[i][j+1]==0):
                        matriz[i][j+1]=matriz[i][j]
                        matriz[i][j] = 0
                    elif(matriz[i][j]==matriz[i][j+1]):
                        matriz[i][j+1]+=matriz[i][j] 
                        matriz[i][j] = 0

    if keys[pygame.K_DOWN]:
        criarNumAleatorio()
        for k in range(5):
            for i in range(4):
                for j in range(5):
                    if(matriz[i+1][j]==0):
                        matriz[i+1][j]=matriz[i][j]
                        matriz[i][j] = 0
                    elif(matriz[i][j]==matriz[i+1][j]):
                        matriz[i+1][j]+=matriz[i][j] 
                        matriz[i][j] = 0
    if keys[pygame.K_UP]:
        criarNumAleatorio()
        for k in range(5):
            for i in range(4):
                for j in range(5):
                    if(matriz[i][j]==0):
                        matriz[i][j]=matriz[i+1][j]
                        matriz[i+1][j] = 0
                    elif(matriz[i][j]==matriz[i+1][j]):
                        matriz[i][j]+=matriz[i+1][j] 
                        matriz[i+1][j] = 0                   
    pygame.display.update()

pygame.quit()
