def sumaEnteros(array, i):
    sumatoria = 0
    if i >= len(array):
        return sumatoria

    sumatoria = sumaEnteros(array, 0)
    return array[i]


# main

array = [1, 7, 8, 3, 44, 6, 46]
sumaEnteros(array, 0)
