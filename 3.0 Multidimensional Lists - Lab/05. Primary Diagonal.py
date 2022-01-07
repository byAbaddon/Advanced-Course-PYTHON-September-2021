print(sum([x[i] for i, x in enumerate([list(map(int, input().split())) for _ in range(int(input()))])]))

# ----------------------------------(2)-----------------

# size_matrix = int(input())
# matrix = []
# diagonal_sum = 0
#
# for _ in range(size_matrix):
#     matrix.append([int(x) for x in input().split()])
#
# index = 0
# for row in matrix:
#     diagonal_sum += row[index]
#     index += 1
#
# print(diagonal_sum)

'''
3
11 2 4
4 5 6
10 8 -12
---------------
4
'''
