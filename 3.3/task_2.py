# Инициализация размерности матрицы
n, m = map(int, input().split())

# Создание матрицы размером n на m, заполненной нулями
mapa = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

# Устанавливаем начальное значение
mapa[0][0] = 0

# Заполнение первой колонки
counter = 0
for i in range(1, n + 1):
    if mapa[i - 1][0] == 0 or counter == 1:
        mapa[i][0] = 1
        counter += 1
    else:
        mapa[i][0] = 0
        counter = 0

# Заполнение первой строки
counter = 0
for i in range(1, m + 1):
    if mapa[0][i - 1] == 0 or counter == 1:
        mapa[0][i] = 1
        counter += 1
    else:
        mapa[0][i] = 0
        counter = 0

# Заполнение оставшейся части матрицы
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if mapa[i - 1][j] == 1 and mapa[i][j - 1] == 1:
            mapa[i][j] = 0
        else:
            mapa[i][j] = 1

# Вывод матрицы
# for j in range(m + 1):
#     for i in range(n + 1):
#         print(mapa[i][j], end=' ')
#     print()

if mapa[n][m] == 1:
    print("Win")
else:
    print("Loose")