negativo = 0
for x in range(1, 11):
    valor = float(input("digite um valor:")) # pedir o valores varias vezes
    if valor < 0:
        negativo += 1
print(f"{negativo} valores são negativo")
