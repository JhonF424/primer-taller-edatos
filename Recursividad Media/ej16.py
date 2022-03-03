def nPares(n, cPares):
    if n <= 0:
        return n

    digito = n % 10
    nPares(int(n / 10), cPares)
    if digito % 2 == 0:
        cPares = cPares + 1

    return cPares


print(nPares(1234, 0))
