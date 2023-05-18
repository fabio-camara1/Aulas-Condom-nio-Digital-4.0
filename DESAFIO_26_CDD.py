quantidade = int(input("quantos alunos tem na sala? "))
lista_alunos = []
for x in range(quantidade):
    lista_alunos.append(input("digite o nome dos alunos:"))
nome_busca = input("qual aluno você procura?")
# if nome_busca in lista_alunos:
#    print("o nome esta na lista ")
# else:
#  print("o nome não esta na lista")
for y in range(quantidade):
    if nome_busca == lista_alunos[y]:
        print(y, lista_alunos[y])
