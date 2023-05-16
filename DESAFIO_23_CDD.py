muda_estado = 0
while muda_estado != 6:
    numero1 = int(input("digite o primeiro numero: "))
    numero2 = int(input("digite o segundo numero: "))
    while True:
        valor = input("escolha uma opção: soma-1,subritração-2,multiplicação-3"
                      ",divisão-4,repetir operação-5,sair do programa-6: ")
        if valor == "1":
            print(numero1 + numero2)
        if valor == "2":
            print(numero1 - numero2)
        if valor == "3":
            print(numero1 * numero2)
        if valor == "4":
            print(numero1 / numero2)
        if valor == "5":
            break
        if valor == "6":
            muda_estado = 6
            break
