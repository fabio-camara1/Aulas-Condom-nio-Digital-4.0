valor1 = float(input("digite o primeiro valor a ser dividido:"))
valor2 = float(input("digite o segundo valor a ser dividido:"))
while valor2 == 0:
    print("digite um valor difetente de zero")
    valor2 = float(input("digite novamente o segundo valor:"))
print(f"a media dos valores digitados é{valor1 / valor2}")
