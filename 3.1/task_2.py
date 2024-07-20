def C(n, k):
    if 0 <= k <= n:
        nn = 1
        kk = 1
        for t in range(1, min(k, n - k) + 1):
            nn *= n
            kk *= t
            n -= 1
        return nn // kk
    else:
        return 0
    
def main():
    n, k = map(int, input().split())
    a = C(n, k)
    print(a)

main()