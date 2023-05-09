alunos = int(input("digite o numero de alunos: "))
numeros_alunos = 0
soma_notas = 0
while numeros_alunos < alunos:
    notas = float(input("digite a media dos alunos: "))
    numeros_alunos += 1
    soma_notas += notas
print(f"a media da sala é {soma_notas / alunos}")
