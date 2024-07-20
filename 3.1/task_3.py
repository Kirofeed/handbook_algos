def C(n, k):
    if k >= 0:
        nn = 1
        kk = 1
        for t in range(k):
            nn *= (n + k - 1 - t)
            kk *= (t + 1)
        return nn // kk
    else:
        return 0

def main():
    n, k = map(int, input().split())
    a = C(n, k)
    print(a)

main()
