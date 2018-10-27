vetor = input("digite a mensagem em números: ").split()

criptografia = [' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

print("Descriptografando...")
for i in range(len(vetor)):
    print(criptografia[int(vetor[i])], end='')
