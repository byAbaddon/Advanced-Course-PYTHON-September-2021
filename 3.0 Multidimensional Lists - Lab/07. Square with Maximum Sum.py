row, col = [int(x) for x in input().split(', ')]
matrix = [list(map(int, input().split(', '))) for _ in range(row)]

squ_matrix = [[0, 0], [0, 0]]

for row in range(len(matrix) - 1):
    for col in range(len(matrix[row]) - 1):
        squ_matrix_sum = squ_matrix[0][0] + squ_matrix[0][1] + squ_matrix[1][0] + squ_matrix[1][1]
        big_square_sum = matrix[row][col] + matrix[row][col + 1] + matrix[row + 1][col] + matrix[row + 1][col + 1]

        if big_square_sum > squ_matrix_sum:
            squ_matrix = [[matrix[row][col], matrix[row][col + 1]], [matrix[row + 1][col], matrix[row + 1][col + 1]]]

square_sum = 0
for row in squ_matrix:
    print(*row)
    square_sum += row[0] + row[1]

print(square_sum)


'''
3, 6
7, 1, 3, 3, 2, 1
1, 3, 9, 8, 5, 6
4, 6, 7, 9, 1, 0
-----------------
9 8
7 9
33

'''