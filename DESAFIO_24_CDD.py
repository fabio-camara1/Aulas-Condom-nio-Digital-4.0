quantidade = int(input("quantos alunos tem na sala? "))
lista_alunos = []
for x in range(quantidade):
    lista_alunos.append(input("digite o nome dos alunos:"))
for y in lista_alunos:
    print(y)
