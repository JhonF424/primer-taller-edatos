count = 1
num = 3


def tablasMulti(count, num):
    if count > 10:
        return;
    
    r = num * count
    print(num, " x ", count, " = ", r)
    tablasMulti(count+1, num)



tablasMulti(count, num)