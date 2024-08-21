


def funk(A):
    m1 = A[0]
    m2 = A[1]
    m3 = A[2]
    if m2 > m1:
        m1, m2 = m2, m1
    if m3 > m2:
        m2, m3 = m3, m2

    for i in range(3, n):
        if A[i] > m1:
            m3 = m2
            m2 = m1
            m1 = A[i]
        else:
            if A[i] > m2:
                m3 = m2
                m2 = A[i]
            else:
                if A[i] > m3:
                    m3 = A[i]
    return (m1 * m2 * m3)

n = int(input())
A = [int(x) for x in input().split()]
A.sort()
A.reverse()

result = A[0] * A[1] * A[2]
if result < A[n - 1] * A[n - 2] * A[0]:
    result = A[n - 1] * A[n - 2] * A[0]

print(result)

# print(funk(A))

