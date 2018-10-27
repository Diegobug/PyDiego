matriz=[[None]*3 for i in range(0,3)]

for i in range(0,3):
    for j in range(0,3):
        matriz[i][j]=int(input(" :"))
        
for i in range(0,3):
    for j in range(0,3):
        if(i==1):
            aux=matriz[i][j]
            matriz[i][j]=matriz[j][i]
            matriz[j][i]=aux
print(matriz)
