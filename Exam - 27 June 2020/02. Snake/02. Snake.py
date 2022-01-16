SIZE = int(input())
matrix = [list(map(str, input())) for _ in range(SIZE)]
snake_pos = [(row, col) for row in range(SIZE) for col in range(SIZE) if matrix[row][col] == 'S'][0]
com_dict = {'up': (-1, 0), 'down': (+1, 0), 'left': (0, -1), 'right': (0, +1)}
apple = 0

while True:
    row, col = snake_pos
    matrix[row][col] = '.'
    com = input()
    row += com_dict[com][0]
    col += com_dict[com][1]

    if 0 <= row < SIZE and 0 <= col < SIZE:
        if matrix[row][col] == 'B':
            matrix[row][col] = '.'
            next_B = [(r, c) for r in range(SIZE) for c in range(SIZE) if matrix[r][c] == 'B'][0]
            row, col = next_B
            matrix[row][col] = 'S'
        elif str(matrix[row][col]) == '-':
            pass
            matrix[row][col] = 'S'
        elif str(matrix[row][col]) == '*':
            matrix[row][col] = 'S'
            apple += 1

        snake_pos = (row, col)
        if apple == 10:
            print(f'You won! You fed the snake.\nFood eaten: 10')
            break
    else:
        print(f'Game over!\nFood eaten: {apple}')
        break

[print(''.join(mtx)) for mtx in matrix]

'''
6
-----S
----B-
------
------
--B---
--*---
left
down
down
down
left

-------------------------
Game over!
Food eaten: 1
----..
----.-
------
------
--.---
--.---

'''

# #------------------------------------------------TODO -------------WTF ???-------- 80pts
# size_matrix = int(input())
# matrix = [row.split() for row in [' '.join(input())for _ in range(size_matrix)]]
# apple = 0
# row, col = 0, 0
#
# for row_index in range(len(matrix)):
#     for col_index in  range(len(matrix[row_index])):
#         if matrix[row_index][col_index] == 'S':
#             matrix[row_index][col_index] = '.'
#             row, col = row_index, col_index
#
# def teleport(row, col):
#         first_B = (row, col)
#         for row_index in range(len(matrix)):
#             for col_index in  range(len(matrix[row_index])):
#                 if matrix[row_index][col_index] == 'B' and (row_index, col_index) != first_B:
#                     second_B = (row_index, col_index)
#                     return second_B
#
# while True:
#     try:
#         direction = input()
#
#         if direction == 'right':
#             col += 1
#         elif direction == 'left':
#             col -= 1
#         elif direction == 'up':
#             row -= 1
#         elif direction == 'down':
#             row += 1
#
#
#         if matrix[row][col] == 'B':
#             matrix[row][col] = '.'
#             row, col = teleport(row, col)
#         elif matrix[row][col] == '*':
#              apple += 1
#              if apple == 10:
#                 matrix[row][col] = 'S'
#                 break
#
#         matrix[row][col] = '.'
#
#     except:
#          break
#
#
# if apple == 10:
#     print(f'You won! You fed the snake.\nFood eaten: 10')
# else:
#     print(f'Game over!\nFood eaten: {apple}')
#
# [print(''.join(mtx)) for mtx in matrix]
