def invertido(num, inv):

    (cociente, residuo) = divmod(num, 10)

    if 0 == cociente:
        return inv * 10 + residuo
    elif 0 == invertido:
        return invertido(cociente, residuo)
    else:
        return invertido(cociente, inv * 10 + residuo)


num = int(input("Número a invertir "))
print("Invertido: ", invertido(num, 0))
