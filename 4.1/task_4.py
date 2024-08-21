n, m = map(int, input().split())

a = []
b = []
for i in range(n):
    a.append([int(x) for x in input().split()])
for i in range(n):
    b.append([int(x) for x in input().split()])


for i in range(n):
    for j in range(m):
        a[i][j] += b[i][j]
        print(a[i][j], end=' ')
    print()

