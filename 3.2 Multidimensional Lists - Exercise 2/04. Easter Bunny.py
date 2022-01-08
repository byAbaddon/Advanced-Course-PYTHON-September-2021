size = int(input())
matrix = [input().split() for _ in range(size)]
bunny = []
statistics_dict = {}

for rows in range(0, size):
    for cols in range(0, size):
        if matrix[rows][cols] == 'B':
            bunny = [rows, cols]


def walking(bunny_pos, direction):
    row, col = bunny_pos
    statistics_dict[direction] = {'steps': [], 'points': 0}
    while True:  # down row++ // up row-- // left col-- // right col++
        if direction == 'down':
            row += 1
        if direction == 'up':
            row -= 1
        if direction == 'left':
            col -= 1
        if direction == 'right':
            col += 1
        if 0 <= row < size and 0 <= col < size and matrix[row][col] != 'X':
            statistics_dict[direction]['steps'].append([row, col])
            statistics_dict[direction]['points'] += int(matrix[row][col])
        else:
            return statistics_dict


walking(bunny, 'right')  # FUCKING IDIOT MAKING TESTS
walking(bunny, 'left')
walking(bunny, 'down')
walking(bunny, 'up')

for k, v in sorted(statistics_dict.items(), key=lambda x: -x[1]['points']):
    print(k, *v['steps'], v['points'], sep='\n')
    break

'''
5
1 3 7 9 11
X 5 4 X 63
7 3 21 95 1
B 1 73 4 9
9 2 33 2 0

--------------
right
[3, 1]
[3, 2]
[3, 3]
[3, 4]
87
'''
