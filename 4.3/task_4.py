
n = int(input())
A = [int(x) for x in input().split()]
A.sort()
A.reverse()

result1 = A[0] * A[1] * A[2] * A[3]
result2 = A[n - 1] * A[n - 2] * A[n - 3] * A[n - 4]
result3 = A[n - 1] * A[n - 2] * A[0] * A[1]


print(max(result1, result2, result3))

# print(funk(A))

