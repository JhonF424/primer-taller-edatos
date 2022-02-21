lista = ["Elemento 1", "Prueba", "Item", "Otra prueba", "ultimo elemento"]

count = len(lista)-1

def listaInvertida(lista, count):
    if count < 0:
        return
    
    print(lista[count])
    listaInvertida(lista, count-1)


listaInvertida(lista, count)