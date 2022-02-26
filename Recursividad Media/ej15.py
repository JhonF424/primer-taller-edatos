def merge(l1, l2, i):

    if i >= len(l1) or i >= len(l2):
        return []

    lAux = []
    lAux.append(l1[i])
    lAux.append(l2[i])
    l3 = merge(l1, l2, i + 1)
    l3.extend(lAux)
    return l3


l1 = [1, 4, 8, 3, 10]
l2 = [6, 2, 9, 7, 8]
print(merge(l1, l2, 0))
