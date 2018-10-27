import random
n=int(input("vamo brincar de dado diga 1 numero:"))
vetor=[None]*n
soma=[0]*6

for i in range(n):
    vetor[i]=random.randint(1,6)
    soma[vetor[i]-1]=soma[vetor[i]-1]+1
print("dados lançados",vetor)
print("apariçao de cara numero em ordem 1,2,3,4,5,6",soma)

for i in range(6):
    p=i+1
    print("a porcentagem da aparição de %d é:" %p,soma[i]/n*100,"%")

