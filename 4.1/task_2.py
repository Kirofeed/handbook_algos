a_deg = int(input())

a_coeff = [int(x) for x in input().split()]

b_deg = int(input())

b_coeff = [int(x) for x in input().split()]

if (a_deg < b_deg):
    a_deg, b_deg = b_deg, a_deg
    a_coeff, b_coeff = b_coeff, a_coeff


for i in range(b_deg + 1):
    a_coeff[a_deg - i] += b_coeff[b_deg - i]

print(len(a_coeff) - 1)
for i in a_coeff:
    print(i, end=' ')
