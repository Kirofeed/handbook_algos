
n = int(input())

A = [n]
for i in range(1, n):
    A.append(i)


def funk(A, n):
    counter = 0
    if n <= 2:
        return counter
    m1 = A[0]
    m2 = A[1]
    if m2 > m1:
        m1, m2 = m2, m1
    counter += 1

    for i in range(2, n):
        counter += 1
        if A[i] > m1:
            m2 = m1
            m1 = A[i]
        else:
            if A[i] > m2:
                counter += 1
                m2 = A[i]
    return counter

counter = funk(A, n)
if counter > n * 1.5:
    print("Yes")
    for i in A:
        print(i, end=' ')
else:
    print("No")