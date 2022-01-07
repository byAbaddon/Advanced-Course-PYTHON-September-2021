matrix_size = int(input())
left, right = 0, 0

for i in range(matrix_size):
    row = [int(x) for x in input().split()]
    left += row[i]
    right += row[len(row) - 1 - i]

print(abs(left - right))


'''
3
11 2 4
4 5 6
10 8 -12
------------------
15
'''