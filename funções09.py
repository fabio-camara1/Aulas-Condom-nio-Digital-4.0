def lista_unica(l):
    nova_lista = []
    for x in l:
        if x not in nova_lista:
            nova_lista.append(x)
    print(nova_lista)


a = [1, 2, 2, 3, 4, 5, 3, 6, 7, 6, 8]

lista_unica(a)
