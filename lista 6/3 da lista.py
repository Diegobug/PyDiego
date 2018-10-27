matriz=[[None]*3 for i in range(0,2)]
vetor=[0]*3

for i in range(0,2):
    for j in range(0,3):
        matriz[i][j]=int(input(" "))
        vetor[j]=vetor[j]+matriz[i][j]

print(vetor)
        
