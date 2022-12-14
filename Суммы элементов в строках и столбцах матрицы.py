from random import randint

M = 7
N = 5
matrix = []
row_sums = [0] * N
col_sums = [0] * M

for i in range(N):
    row = []
    for j in range(M):
        row.append(randint(0,3))
    matrix.append(row)

for i in range(N):
    for j in range(M):
        row_sums[i] += matrix[i][j] # см. тетрадь
        col_sums[j] += matrix[i][j]

for i in range(N):
    print(matrix[i], '|', row_sums[i])
print('-' * M * 4)
print(col_sums)