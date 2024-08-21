def find_best(spicies):
    max = (0, 0)
    for i in range(len(spicies)):
        if i == 0:
            max = spicies[0]
        else:
            if (spicies[i][0]/spicies[i][1] > max[0]/max[1]):
                max = spicies[i]
    if max != (0, 0):
        return max
    

n, max_weight = map(int, input().split())
spicies = []
for i in range(n):
    price, weight = map(int, input().split())
    data = (price, weight)
    if i == 0:
        max = data
    else:
        if (data[0]/data[1] > max[0]/max[1]):
            max = data
    spicies.append(data)


current_weight = 0
total_price = 0
i = 0
while current_weight < max_weight and len(spicies) != 0:
    if max_weight - current_weight <= max[1]:
        total_price += (max[0]/max[1]) * (max_weight - current_weight)
        current_weight += max_weight - current_weight
    else:
        total_price += (max[0]/max[1]) * max[1]
        current_weight += max[1]
    spicies.remove(max)
    max = find_best(spicies)
    i += 1

print(f'{total_price:.3f}')