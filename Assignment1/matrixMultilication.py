A = [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]
B = [[9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]]
# Result matrix initialized with zeros
result = [[0 for _ in range(3)] for _ in range(3)]
for i in range(3):
    for j in range(3):
        for k in range(3):
            result[i][j] += A[i][k] * B[k][j]

# Print result
print("Matrix Product:")
for row in result:
    print(row)
