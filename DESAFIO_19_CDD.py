senha_programa = "123"
falhas = 0
senha_usuario = input("digite a sua senha")
while senha_usuario != senha_programa:
    falhas += 1
    print("senha incorreta")
    senha = input()
    if falhas > 2 and senha != senha_programa:
        print("senha bloqueada")
        break
else:
    print("sua senha esta errada")
