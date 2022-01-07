matrix = [list(map(int, input().split())) for _ in range(int(input()[0]))]
index = 0

while True:
    try:
        col_sum = 0
        for i in range(len(matrix)):
            col_sum += matrix[i][index]
        print(col_sum)
        index += 1
    except:
        break

# ----------------------------(2)------------------------------

# row, col = [int(x) for x in input().split(', ')]
# matrix = []
# index = 0
#
# for _ in range(row):
#     matrix.append([int(x) for x in input().split()])
#
# while True:
#     matrix_col_sum = 0
#     for i in range(len(matrix)):
#         matrix_col_sum += matrix[i][index]
#
#     print(matrix_col_sum)
#     index += 1
#
#     if index == col:
#         break


'''
3, 6
7 1 3 3 2 1
1 3 9 8 5 6
4 6 7 9 1 0
---------------------
12
10
19
20
8
7
'''
