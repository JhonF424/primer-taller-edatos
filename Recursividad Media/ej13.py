def repite(lista, i, busq):
    if i >= len(lista):
        return 0
    num = lista[i]
    cuantas = repite(lista, i + 1, busq)

    if busq == num:
        cuantas += 1

    return cuantas


lista = [10, 3, 65, 6, 1, 80, 6]
print("Veces que se repite: ", repite(lista, 0, 6))
