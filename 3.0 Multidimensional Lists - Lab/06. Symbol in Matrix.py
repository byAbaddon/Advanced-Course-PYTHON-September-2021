matrix = [(i, [list(enumerate(x)) for x in input().split()]) for i in range(int(input()))]
symbol = input()
try:
    row, col = [x for x in [[row[0], [x[0] for x in row[1][0] if x[1] == symbol]] for row in matrix] if x[1] != []][0]
    print((row, col[0]))
except:
    print(symbol, 'does not occur in the matrix')

#
# ----------------------------------------(2)----------------------
# size_matrix = int(input())
# matrix = []
#
# for _ in range(size_matrix):
#     matrix.append(input())
#
# symbol = input()
#
# for row in range(len(matrix)):
#     for col in range(len(matrix[row])):
#         if matrix[row][col] == symbol:
#             print((row,col))
#             exit()
#
# print(symbol, 'does not occur in the matrix')


'''
3
ABC
DEF
X!@
!
--------------------
(2, 1)
'''
