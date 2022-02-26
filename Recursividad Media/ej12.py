def menor(vector, i):
    if i >= len(vector):
        return vector[i - 1]

    num = vector[i]
    aux = menor(vector, i + 1)

    if num < aux:
        aux = num

    return aux


vector = [10, 3, 65, 6, 1, 80]
print("Menor: ", menor(vector, 0))
