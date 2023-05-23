nomes = []
senhas = []
for x in range(5):
    nomes.append(input("digite o nome:"))
    senhas.append(input("digite a senha:"))
for y in range(5):
    print(y, nomes[y], senhas[y])
