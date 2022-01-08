size = int(input())
matrix = [input().split() for _ in range(size)]
alice = ()
tea = 0

for rows in range(0, size):
    for cols in range(0, size):
        if matrix[rows][cols] == 'A':
            alice = (rows, cols)


while True:  # down row++ // up row-- // left col-- // right col++
    row, col = alice
    matrix[row][col] = '*'
    direction = input()

    if direction == 'down':
        row += 1
    if direction == 'up':
        row -= 1
    if direction == 'left':
        col -= 1
    if direction == 'right':
        col += 1
    if 0 <= row < size and 0 <= col < size:
        alice = (row, col)
        if matrix[row][col] == 'R':
            matrix[row][col] = '*'
            break
        if matrix[row][col].isdigit():
            tea += int(matrix[row][col])
            if tea >= 10:
                matrix[row][col] = '*'
                break
        matrix[row][col] = '*'
    else:
        break

if tea >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")
[print(*r) for r in matrix]


'''
5
. A . . 1
R . 2 . .
4 7 . 1 .
. . . 2 .
. 3 . . .
down
right
left
down
up
left
---------------------------
Alice didn't make it to the tea party.
. * . . 1
* * * . .
4 * . 1 .
. . . 2 .
. 3 . . .
'''
