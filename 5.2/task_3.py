def NumsByFibanacci(n):
    if n == 1:
        return (1, 1)
    a, b = 1, 0
    while True:
        if (a + b) <= n:
            if (a < b):
                a += b
            else:
                b += a
        else:
            break
    return (min(a, b), max(a, b))

n = int(input())

a, b = NumsByFibanacci(n)

print(a, ' ', b)
