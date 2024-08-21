n = int(input())
list = [int(x) for x in input().split()]

max1 = 0
max2 = 0
for i in list:
    if i > max1:
        max1 = i
list.remove(max1)
for i in list:
    if i > max2:
        max2 = i

print(max1 * max2)