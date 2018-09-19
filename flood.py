import pygame
import sys
import random
import numpy

pygame.init()
#declaracao de variaveis
screen = pygame.display.set_mode((640,480))
pygame.display.set_caption("flood fill")
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
pink = (255,200,200)
screen.fill(pink)
colors = [red,green,blue,darkBlue,white,black] #cores
matriz = [[0 for x in range(10)] for y in range(10)] #matriz

#funcao de floodar
def flood(cor_alvo,matriz,i,j,nova_cor):
    if(matriz[i][j]!=cor_alvo or cor_alvo == nova_cor):
        return
    elif(0<=i<9 and 0<=j<9):
        matriz[i][j] = nova_cor
        flood(cor_alvo,matriz,i+1,j,nova_cor)
        flood(cor_alvo,matriz,i,j+1,nova_cor)
        flood(cor_alvo,matriz,i-1,j,nova_cor)
        flood(cor_alvo,matriz,i,j-1,nova_cor)

#preenche a matriz de forma aleatoria       
for i in range(0,9):
    for j in range(0,9):
        matriz[i][j] = random.randint(0,5)
        
sair = True

while sair:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sair = False   
        for i in range(0,9):
            for j in range(0,9):
                pygame.draw.rect(screen, colors[matriz[i][j]], (i*50,j*50,50,50), 0)

        keys=pygame.key.get_pressed()
        if keys[pygame.K_0]:
            flood(matriz[0][0],matriz,0,0,0)
        if keys[pygame.K_1]:
            flood(matriz[0][0],matriz,0,0,1)
        if keys[pygame.K_2]:
            flood(matriz[0][0],matriz,0,0,2)
        if keys[pygame.K_3]:
            flood(matriz[0][0],matriz,0,0,3)
        if keys[pygame.K_4]:
            flood(matriz[0][0],matriz,0,0,4)
        if keys[pygame.K_5]:
            flood(matriz[0][0],matriz,0,0,5)    
        pygame.display.update()
    
pygame.quit()

    


