import random

def Lomuto(list):
    if len(list) == 1 or len(list) == 0:
        return list
    pivot_index = random.randint(0, len(list) - 1)
    list[0], list[pivot_index] = list[pivot_index], list[0]
    pivot = list[0]
    border_index = 0
    for i in range (1, len(list)):
        if list[i] < pivot:
            border_index += 1
            list[border_index], list[i] = list[i], list[border_index]
    list[0], list[border_index] = list[border_index], list[0]
    first_part = Lomuto(list[:border_index])
    second_part = Lomuto(list[(border_index + 1):])
    list = first_part
    list.append(pivot)
    list += second_part
    return list


n = input()
listik  = [int(x) for x in input().split()]
listik = Lomuto(listik)
for i in listik:
    print(i, end=' ')

