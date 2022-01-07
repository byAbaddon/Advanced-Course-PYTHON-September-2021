def is_valid_index(matrix, i_index, j_index):
    if 0 <= i_index < len(matrix) and 0 <= j_index < len(matrix[0]):
        return True
    else:
        return False


n = int(input())

bomb_zone = []
for _ in range(n):
    bomb_zone.append(list(map(int, input().split())))

coordinates = [list(map(int, el.split(','))) for el in input().split()]

for position in coordinates:
    i = position[0]
    j = position[1]
    if bomb_zone[i][j] <= 0:
        break
    magnitude = bomb_zone[i][j]
    bomb_zone[i][j] = 0
    if is_valid_index(bomb_zone, i - 1, j) and bomb_zone[i - 1][j] > 0:
        bomb_zone[i - 1][j] = bomb_zone[i - 1][j] - magnitude
    if is_valid_index(bomb_zone, i - 1, j + 1) and bomb_zone[i - 1][j + 1] > 0:
        bomb_zone[i - 1][j + 1] = bomb_zone[i - 1][j + 1] - magnitude
    if is_valid_index(bomb_zone, i, j + 1) and bomb_zone[i][j + 1] > 0:
        bomb_zone[i][j + 1] = bomb_zone[i][j + 1] - magnitude
    if is_valid_index(bomb_zone, i + 1, j + 1) and bomb_zone[i + 1][j + 1] > 0:
        bomb_zone[i + 1][j + 1] = bomb_zone[i + 1][j + 1] - magnitude
    if is_valid_index(bomb_zone, i + 1, j) and bomb_zone[i + 1][j] > 0:
        bomb_zone[i + 1][j] = bomb_zone[i + 1][j] - magnitude
    if is_valid_index(bomb_zone, i + 1, j - 1) and bomb_zone[i + 1][j - 1] > 0:
        bomb_zone[i + 1][j - 1] = bomb_zone[i + 1][j - 1] - magnitude
    if is_valid_index(bomb_zone, i, j - 1) and bomb_zone[i][j - 1] > 0:
        bomb_zone[i][j - 1] = bomb_zone[i][j - 1] - magnitude
    if is_valid_index(bomb_zone, i - 1, j - 1) and bomb_zone[i - 1][j - 1] > 0:
        bomb_zone[i - 1][j - 1] = bomb_zone[i - 1][j - 1] - magnitude

alive_cells = 0
alive_cells_sum = 0
for i in range(n):
    for j in range(n):
        if bomb_zone[i][j] > 0:
            alive_cells += 1
            alive_cells_sum += bomb_zone[i][j]

print(f"Alive cells: {alive_cells}")
print(f"Sum: {alive_cells_sum}")
for i in range(n):
    for j in range(n):
        print(bomb_zone[i][j], end=' ')
    print()



'''
4
8 3 2 5
6 4 7 9
9 9 3 6
6 8 1 2
1,2 2,1 2,0
----------------------------
Alive cells: 3
Sum: 12
8 -4 -5 -2
-3 -3 0 2
0 0 -4 -1
-3 -1 -1 2

'''