row, col = [int(x) for x in input().split()]
matrix = [list(map(int, input().split())) for _ in range(row)]
square_matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for row in range(len(matrix) - 2):
    for col in range(len(matrix[row]) - 2):
        square_matrix_sum = square_matrix[0][0] + square_matrix[0][1] + square_matrix[0][2] + \
                            square_matrix[1][0] + square_matrix[1][1] + square_matrix[1][2] + \
                            square_matrix[2][0] + square_matrix[2][1] + square_matrix[2][2]

        big_square_sum = matrix[row][col] + matrix[row][col + 1] + matrix[row][col + 2] + \
                         matrix[row + 1][col] + matrix[row + 1][col + 1] + matrix[row + 1][col + 2] + \
                         matrix[row + 2][col] + matrix[row + 2][col + 1] + matrix[row + 2][col + 2]

        if big_square_sum > square_matrix_sum:
            square_matrix = [[matrix[row][col], matrix[row][col + 1], matrix[row][col + 2]], \
                             [matrix[row + 1][col], matrix[row + 1][col + 1], matrix[row + 1][col + 2]], \
                             [matrix[row + 2][col], matrix[row + 2][col + 1], matrix[row + 2][col + 2]]
                             ]

square_sum = 0
for row in square_matrix:
    square_sum += row[0] + row[1] + row[2]
print('Sum =', square_sum)
[print(*row) for row in square_matrix]

'''
4 5
1 5 5 2 4
2 1 4 14 3
3 7 11 2 8
4 8 12 16 4
-----------------
Sum = 75
[1, 4, 14]
[7, 11, 2]
[8, 12, 16]
'''