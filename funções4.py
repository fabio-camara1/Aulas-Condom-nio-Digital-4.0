def estoque(nome, quantidade, valor, unidade):
    return nome, quantidade, (quantidade * valor), unidade


total = estoque("banana", 30, 3.5, 3.5)
print(f"o produto {total[0]} custa {total[3]} comprando {total[1]} o total é {total[2]}")
