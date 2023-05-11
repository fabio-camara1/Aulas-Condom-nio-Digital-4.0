while True:
    while True:
        avaliação1 = float(input("digite a primeira nota"))
        if avaliação1 >= 0 and avaliação1 <= 10: break
    while True:
        avaliação2 = float(input("digite a segunda nota"))
        if 0 <= avaliação2 <= 10: break
        resultado = (avaliação2 + avaliação1) / 2
        print(f"a media do aluno é{resultado}")
    continuação =input("deseja fazer um novo calculo para sim digite [1] para não digit [2]")
    if continuação == 1:
        print("okay")

    else:
        print("ok")
        break
