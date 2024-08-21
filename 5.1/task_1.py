def GetFibanacci(n):
    i = 0
    fibanacci = 0
    prev = 0
    while (i <= n):
        if i == 1:
            fibanacci = 1
            prev = 0
        else:
            prev, fibanacci = fibanacci, fibanacci + prev
        i += 1
    return fibanacci

n = int(input())
print(GetFibanacci(n))