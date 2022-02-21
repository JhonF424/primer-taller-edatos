lista = ["Dato 1", "Dato 2", "Dato 3", "Dato 4", "Dato 5"]
count = 0
def leer_lista(lista, count):
    if count >= len(lista):
        return

    print(lista[count])

    leer_lista(lista, count+1)

leer_lista(lista, count)