def GetFibanacciLastNum(n):
    i = 0
    fibanacci = 0
    prev = 0
    while (i <= ((n+2) % 60)):
        if i == 1:
            fibanacci = 1
            prev = 0
        else:
            prev, fibanacci = fibanacci, (fibanacci + prev) % 10
        i += 1
    if fibanacci == 0:
        return 9
    else:
        return fibanacci - 1

m, n = map(int, input().split())
first_inter = GetFibanacciLastNum(n)
if m >= 1:
    second_inter = GetFibanacciLastNum(m - 1)
else:
    second_inter = 0

result = first_inter - second_inter

if result < 0:
    result += 10

print(result)