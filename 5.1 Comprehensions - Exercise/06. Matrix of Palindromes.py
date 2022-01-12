row, col = [int(x) for x in input().split()]
matrix = ([[f'{chr(i)}{chr(i + j)}{chr(i)}' for j in range(col)] for i in range(97, row + 97)])

for row in matrix:
    print(*row)


