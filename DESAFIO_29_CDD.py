# numeros = []
# for x in range(5):
#    numeros.append(int(input("digite aqui um valor:")))
# numeros.reverse()
# print(numeros)
vetor = []
for x in range(5):
    vetor.append(int(input("digite um numero:")))
for j in range(5):
    print(vetor[4-j], end=" ")
