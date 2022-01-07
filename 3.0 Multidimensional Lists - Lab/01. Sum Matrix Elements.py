matrix = [list(map(int, input().split(', '))) for _ in range(int(input()[0]))]
print(sum([sum(x) for x in matrix]), matrix, sep='\n')

# ----------------------(2)--------------

# row, col = [int(x) for x in input().split(', ')]
# matrix = []
# matrix_sum = 0
#
# for i in range(row):
#     matrix.append([int(x) for x in input().split(', ')])
#     matrix_sum += sum(matrix[i])
#
# print(matrix_sum)
# print(matrix)

'''
3, 6
7, 1, 3, 3, 2, 1
1, 3, 9, 8, 5, 6
4, 6, 7, 9, 1, 0

----------------------
76
[[7, 1, 3, 3, 2, 1], [1, 3, 9, 8, 5, 6], [4, 6, 7, 9, 1, 0]]

'''
