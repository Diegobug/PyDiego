altura = [None]*10
sexo = [None]*10

alturaMaior = 0
alturaMenor = 3#poderia ser qualquer numero maior que dois

sexoDoMaior=''
sexoDoMenor=''

contadorMasculino = 0
contadorFeminino = 0

somaAlturaMasculina = 0
somaAlturaFeminina = 0

for i in range(len(altura)):
    altura[i] = float(input("altura da pessoa %d: " %i))
    sexo[i] = input("sexo da pessoa %d (M ou F): " %i)

    if(altura[i] > alturaMaior):
        alturaMaior = altura[i]
        sexoDoMaior = sexo[i]
    if(altura[i] < alturaMenor):
        alturaMenor = altura[i]
        sexoDoMenor = sexo[i]

    if(sexo[i]=='f' or sexo[i]=='F'):
        contadorFeminino+=1
        somaAlturaFeminina+=altura[i]
    elif(sexo[i]=='m' or sexo[i]=='M'):
        contadorMasculino+=1
        somaAlturaMasculina+=altura[i]


        
print("O maior tem %.2f de altura e é do sexo %s" %(alturaMaior,sexoDoMaior))
print("O menor tem %.2f de altura e é do sexo %s" %(alturaMenor,sexoDoMenor))
if(contadorMasculino!=0):
    print("Media de altura masculina: %.4f" %(somaAlturaMasculina/contadorMasculino))
if(contadorFeminino!=0):
    print("Media de altura feminina: %.4f" %(somaAlturaFeminina/contadorFeminino))
print("Total de Homens: %d" %contadorMasculino)
print("Total de Mulheres: %d" %contadorFeminino)


