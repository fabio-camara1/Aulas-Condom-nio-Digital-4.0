valores = []
for x in range(10):
    valores.append(int(input("digite os valores")))
for y in range(10):
    if valores[y] % 2 == 0:
        print(valores[y])
maior = valores[0]
menor = valores[0]
for z in range(11):
    if z > maior:
        maior = z
    elif z < menor:
        menor = z
print(f"o maior valor do vetor é {maior}")
print(f"o menor valor do vetor é {menor}")
media = sum(valores)/10
conta = 0
for w in range(10):
    if valores[w] > media:
        conta = conta + 1
print(f"a quantidade de numeros maiores que a media de{valores} é {conta}")
