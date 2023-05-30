tamanho_do_vetor = int(input("digite o tamanho do vetor:"))
vetorA = []
vetorB = []
vetorC = []
for x in range(tamanho_do_vetor):
    vetorA.append(int(input("digite aqui os valores do primeiro vetor")))
    vetorB.append(int(input("digite os valores do segundo vetor")))
for y in range(tamanho_do_vetor):
    vetorC.append(vetorA[y] + vetorB[y])
print(vetorA)
print(vetorB)
print(vetorC)
