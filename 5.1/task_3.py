def GetFibanacciLastNum(n, m):
    i = 0
    fibanacci = 0
    prev = 0
    while (i <= n):
        if i == 1:
            fibanacci = 1
            prev = 0
        else:
            prev, fibanacci = fibanacci, (fibanacci + prev) % m
        i += 1
    return fibanacci

def PisanoPeriod(m):
    current = 0
    next = 1
    period = 0
    while True:
        old_next = next
        next = (current + next) % m
        current = old_next
        period += 1
        if current == 0 and next == 1:
            return period
    


n, m = map(int, input().split())

print(GetFibanacciLastNum(n % (PisanoPeriod(m)), m))

