num_of_rings = int(input())

list = []
def recursive_def_for_rings(num_of_rings, peg_from, peg_to, list):
    if num_of_rings == 1:
        list.append([peg_from, peg_to])
        return
    peg_other = 6 - peg_from - peg_to
    recursive_def_for_rings(num_of_rings - 1, peg_from, peg_other, list)
    list.append([peg_from, peg_to])
    recursive_def_for_rings(num_of_rings - 1, peg_other, peg_to, list)

recursive_def_for_rings(num_of_rings, 1, 3, list)

print(len(list))
for i in list:
    print(i[0], ' ', i[1])