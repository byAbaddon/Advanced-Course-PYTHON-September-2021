matrix = [list(map(int, input().split(', '))) for x in range(int(input()))]
rev_matrix = [list(reversed(x)) for x in matrix]
pr = [matrix[i][i] for i in range(len(matrix))]
se = [rev_matrix[i][i] for i in range(len(rev_matrix))]

print(f'Primary diagonal: {", ".join([str(x) for x in pr])}. Sum: {sum(pr)}')
print(f'Secondary diagonal: {", ".join([str(x) for x in se])}. Sum: {sum(se)}')


# -----------------------------(2)----------------------

# size = int(input())
# matrix = [input().split(', ') for x in range(size)]
# pr = se = ''
# for i in range(len(matrix)):
#     pr += matrix[i][i]
#     se += matrix[i][size - 1 - i]
#
# print(f'Primary diagonal: {", ".join(pr)}. Sum: {eval("+".join(pr))}')
# print(f'Secondary diagonal: {", ".join(se)}. Sum: {eval("+".join(se))}')

'''
3
1, 2, 3
4, 5, 6
7, 8, 9
--------------
Primary diagonal: 1, 5, 9. Sum: 15
Secondary diagonal: 3, 5, 7. Sum: 15

'''
