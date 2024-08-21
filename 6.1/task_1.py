def Change(money):
    combinations = []
    i_10, i_5 = 0, 0
    combination = ""
    counter = 0
    while(i_10 * 10 <= money):
        while(i_5 * 5 <= money - i_10 * 10):
            counter = i_10 + i_5 + (money - i_10 * 10 - i_5 * 5)
            combination += (str(counter) + " ")
            for i in range(money - i_10 * 10 - i_5 * 5):
                combination += "1 "
            for i in range(i_5):
                combination += "5 "
            for i in range(i_10):
                combination += "10 "
            combinations.append(combination)
            combination = ""
            i_5 += 1
        i_5 = 0
        i_10 += 1
    combinations.reverse()
    print_combinations(combinations)

def print_combinations(combinations):
    # Сначала выводим количество наборов
    print(len(combinations))
    for i in combinations:
        print(str(i).strip())





money = int(input())

Change(money)

