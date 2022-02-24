def sumaPares(num, suma):
    if num < 2:
        return 0

    suma = sumaPares(num - 1, suma)
    if num % 2 == 0:
        print("Numero: ", num)
        suma += num

    return suma


# main

num = 20
suma = 0
print("Resultado: ", sumaPares(num, suma))
