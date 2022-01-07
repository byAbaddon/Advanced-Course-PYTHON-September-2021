def get_damage(row, col, matrix):  # copy / paste - code
    counter = 0
    if row - 2 >= 0 and col - 1 >= 0:
        if matrix[row - 2][col - 1] == 'K':
            counter += 1
    if row - 2 >= 0 and col + 1 < len(matrix):
        if matrix[row - 2][col + 1] == 'K':
            counter += 1
    if row - 1 >= 0 and col - 2 >= 0:
        if matrix[row - 1][col - 2] == 'K':
            counter += 1
    if row - 1 >= 0 and col + 2 < len(matrix):
        if matrix[row - 1][col + 2] == 'K':
            counter += 1
    if row + 1 < len(matrix) and col - 2 >= 0:
        if matrix[row + 1][col - 2] == 'K':
            counter += 1
    if row + 1 < len(matrix) and col + 2 < len(matrix):
        if matrix[row + 1][col + 2] == 'K':
            counter += 1
    if row + 2 < len(matrix) and col - 1 >= 0:
        if matrix[row + 2][col - 1] == 'K':
            counter += 1
    if row + 2 < len(matrix) and col + 1 < len(matrix):
        if matrix[row + 2][col + 1] == 'K':
            counter += 1
    return counter


row_count = int(input())
matrix = []
positon = []
deleted_knights = 0

for i in range(row_count):
    matrix.append([i for i in input()])

while True:
    max_damage = 0
    for row in range(row_count):
        for col in range(row_count):
            current = matrix[row][col]
            if current == 'K':
                damage = get_damage(row, col, matrix)
                if damage > max_damage:
                    max_damage = damage
                    position = [row, col]
    if max_damage == 0:
        break

    first_pos = position[0]
    second_pos = position[1]
    matrix[first_pos][second_pos] = '0'
    position = []
    deleted_knights += 1

print(deleted_knights)
