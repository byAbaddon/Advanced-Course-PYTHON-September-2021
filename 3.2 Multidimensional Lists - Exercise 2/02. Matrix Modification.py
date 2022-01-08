matrix = [[int(x) for x in input().split()] for _ in range(int(input()))]

while True:
    token = input()
    if token == 'END':
        [print(*row) for row in matrix]
        exit()
    try:
        com, row, col, val = list(map(lambda x: int(x) if x.isdigit() else x, token.split()))

        if com == 'Add':
            matrix[row][col] += val
        elif com == 'Subtract':
            matrix[row][col] -= val
    except:
        print('Invalid coordinates')


'''
4
1 2 3 4
5 6 7 8
8 7 6 5
4 3 2 1
Add 4 4 100
Add 3 3 100
Subtract -1 -1 42
Subtract 0 0 42
END
------------------------------

Invalid coordinates
-41 2 3 4
5 6 7 8
8 7 6 5
4 3 2 101
'''