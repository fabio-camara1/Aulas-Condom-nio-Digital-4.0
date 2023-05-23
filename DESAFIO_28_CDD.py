vetorA = []
for x in range(10):
    vetorA.append(int(input("digite os valores:")))
variavelX = int(input("digite um numero:"))
vetorM = []
for y in range(10):
    vetorM.append(vetorA[y] * variavelX)
print(f"lista de valores\n{vetorA}")
print(variavelX)
print(vetorM)
