def primo(num, i):
    r = 0
    if i <= 2:
        return num

    if num % i == 0:
        r = 1

    t = primo(num, num - 1)
    t = t + r

    if t > 1:
        print("No es")

    return t


print("Es primo?", primo(8, 0))
