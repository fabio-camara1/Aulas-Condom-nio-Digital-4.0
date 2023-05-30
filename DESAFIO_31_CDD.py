nomes = []
senhas = []
for x in range(2):
    nomes.append(input("digite o nome:"))
    senhas.append(input("digite a senha:"))
usuario = input("digite o usuario:")
codigo = input("digite o codigo:")
for y in range(2):
    if nomes[y] == usuario and senhas[y] == codigo:
        print("acesso liberado")
        break
else:
    print("acesso negado")
