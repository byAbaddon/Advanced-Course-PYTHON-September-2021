rows, cols = [int(x) for x in input().split()]
matrix = [input().split() for _ in range(rows)]

while True:
    token = input().split()

    if len(token) == 1:
        break
    elif 'swap' not in token:
        print('Invalid input!')
    elif len(token) == 5:
        swap, row1, col1, row2, col2 = [int(x) if x.isdigit() else x for x in token]
        if row1 <= rows and row2 <= rows and col1 <= cols and col2 <= cols:
            first_change = matrix[row1][col1]
            second_change = matrix[row2][col2]
            matrix[row1][col1] = second_change
            matrix[row2][col2] = first_change
            [print(*row) for row in matrix]
        else:
            print('Invalid input!')
    else:
        print('Invalid input!')


'''
2 3
1 2 3
4 5 6
swap 0 0 1 1
swap 10 9 8 7
swap 0 1 1 0
END
---------------
5 2 3
4 1 6
Invalid input!
5 4 3
2 1 6
'''