def GetFibanacciLastNum(n):
    i = 0
    fibanacci = 0
    prev = 0
    while (i <= n):
        if i == 1:
            fibanacci = 1
            prev = 0
        else:
            prev, fibanacci = fibanacci, (fibanacci + prev) % 10
        i += 1
    return fibanacci

n = int(input())
print(GetFibanacciLastNum(n))