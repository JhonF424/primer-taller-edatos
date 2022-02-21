enteros = [1, 5, 9, 7, 4, 2, 3, 10, 6, 8]

count = 0

print("Lista inicial: ", enteros)


def burbuja(enteros, count):
    if count >= len(enteros) -1:
        return

    if enteros[count] < enteros[count + 1]:
        aux = enteros[count]
        # print("aux: ", aux)
        # print("El número de la derecha es: ", enteros[count + 1])
        enteros[count] = enteros[count + 1]
        # print("ahora el de la derecha es igual al auxiliar")
        enteros[count + 1] = aux
        # print(enteros)
        burbuja(enteros, count)

    burbuja(enteros, count + 1)


burbuja(enteros, count)
print("Lista ordenada: ", enteros)
