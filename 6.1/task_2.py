def Change(money):
    i_50 = money // 50
    money -= i_50 * 50
    i_20 = money // 20
    money -= i_20 * 20
    i_10 = money // 10
    money -= i_10 * 10
    i_5 = money // 5
    money -= i_5 * 5
    i_1 = money // 1
    money -= i_1 * 1
    print_combinations(i_1, i_5, i_10, i_20, i_50)

def print_combinations(i_1, i_5, i_10, i_20, i_50):
    result = ""
    print (i_1 + i_5 + i_10 + i_20 + i_50)
    for i in range(i_50):
        result += "50 "
    for i in range(i_20):
        result += "20 "
    for i in range(i_10):
        result += "10 "
    for i in range(i_5):
        result += "5 "
    for i in range(i_1):
        result += "1 "
    print(str(result).strip())


money = int(input())
Change(money)


