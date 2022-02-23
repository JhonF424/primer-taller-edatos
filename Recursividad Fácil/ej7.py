def sumaEnteros(array, i):
    if i >= len(array):
        return []
    suma = 0
    sumatoria = sumaEnteros(array, i + 1)
    suma = suma + sumatoria
    return sumatoria
    


# main

array = [1, 7, 8, 3, 44, 6, 46]
print("Resultado: ", sumaEnteros(array, 0))
