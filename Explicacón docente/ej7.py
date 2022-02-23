def invertir(lista, count):
    
    if count >= len(lista):
        return []
    listaN = []
    listaN.append(lista[count])
    listaA = invertir(lista, count + 1)
    listaA.extend(listaN)
    return listaA


# main
lista = [40, 20, 10, 5]
print(invertir(lista, 0))
