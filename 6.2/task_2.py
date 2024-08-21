n, money = map(int, input().split())
data = []
for i in range(n):
    suv = int(input())
    data.append(suv)
data.sort()

counter = 0
while(money >= 0 and len(data) != 0):
    if money >= data[0]:
        money -= data[0]
        counter += 1
        data.pop(0)
    else:
        break

print(counter)