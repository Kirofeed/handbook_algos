def Merge(list1, list2):
    sorted_list = []
    i, j = 0, 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            sorted_list.append(list1[i])
            i += 1
        else:
            sorted_list.append(list2[j])
            j += 1
    
    while i < len(list1):
        sorted_list.append(list1[i])
        i += 1
    while j < len(list2):
        sorted_list.append(list2[j])
        j += 1

    return sorted_list

def MergeSort(list):
    if len(list) == 1:
        return list

    mid_index = len(list) // 2
    first_half = list[:mid_index]
    second_half = list[mid_index:]
    sorted_first_half = MergeSort(first_half)
    sorted_second_half = MergeSort(second_half)
    return Merge(sorted_first_half, sorted_second_half)

list = []

# Ввод количества отсортированных последовательностей
n = int(input())

# Список для хранения всех последовательностей
sequences = []

# Чтение каждой последовательности
for _ in range(n):
    # Ввод количества элементов в текущей последовательности
    mi = int(input())
    
    # Ввод элементов последовательности и преобразование их в список целых чисел
    sequence = [int(x) for x in input().split()]
    
    sequences.append(sequence)

for i in sequences:
    list = Merge(list, i)

for i in list:
    print(i, end = ' ')