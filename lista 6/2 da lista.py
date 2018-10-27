n=int(input("Digite o tamanho do vetor:"))
vetor=[None]*n

for i in range(n):
    vetor[i]=int(input("Digite os numeros do vetor:"))
    if(vetor[i]%2==0):
		vetor[i]*=2
	else:
		vetor[i]*=3
		
for i in range(n):
    print (vetor[i])

        
