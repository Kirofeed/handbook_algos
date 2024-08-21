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

n = int(input())
list = [int(x) for x in input().split()]


sorted_list = MergeSort(list)

for i in sorted_list:
    print(i, end=' ')
