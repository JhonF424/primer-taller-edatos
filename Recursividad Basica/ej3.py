lista = [1, 2, 3, 4, "prueba", 6]
count = len(lista) - 1
lInversa = []


def lista_invertida(count, lista):
    if count < 0:
        print("Lista normal: ", lista)
        print("Lista invertida: ", lInversa)
        return

    lInversa.append(lista[count])
    lista_invertida(count - 1, lista)


lista_invertida(count, lista)
