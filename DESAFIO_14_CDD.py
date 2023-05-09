fora = 0
dentro = 0
for x in range(1, 11):
    valor = int(input("digite um valor"))
    if 10 <= valor <= 20:
        dentro += 1
    else:

        fora += 1
print(f"{dentro} estão no intervalo")
print(f"{fora} então fora do intervalo")
