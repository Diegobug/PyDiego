# PyDiego
from random import randint
matriz = [[0 for x in range(10)] for y in range(10)]
        
def criarNumAleatorio():
    x = randint(0,9)
    y = randint(0,9)
    if(matriz[x][y]==0 and matriz[(x+y)%10][(y-x)%10]==0):
        matriz[x][y]=2
        matriz[(x+y)%10][(y-x)%10]=2
        for i in range(10):
            for j in range(10):
                print("",matriz[i][j],end="")
            print()
    else:
        return criarNumAleatorio()
while(True):
    criarNumAleatorio()
    jogada=(input(" A <-  D -> "))

    if(jogada=="a"):
        for i in range(10):
            for j in range(9,0,-1):
                if(matriz[i][j-1]==0):
                    matriz[i][j-1]=matriz[i][j]
                    matriz[i][j] = 0
                elif(matriz[i][j-1]==matriz[i][j]):
                    matriz[i][j-1]+=matriz[i][j] 
                    matriz[i][j] = 0
