count = 0


def saludar(count):
    if count >= 10:
        return

    print("Hola mundo")
    saludar(count + 1)


saludar(count)
