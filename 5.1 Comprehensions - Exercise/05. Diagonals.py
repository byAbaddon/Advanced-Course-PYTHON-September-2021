matrix = [input().split(', ') for x in range(int(input()))]

left_sum, right_sum = 0, 0
for i in range(len(matrix)):
    left_sum += int(matrix[i][i])
    right_sum += int(matrix[i][len(matrix) - 1 - i])

print('First diagonal:', ', '.join([matrix[i][i] for i in range(len(matrix))]) + '.','Sum:', left_sum)
print('Second diagonal:', ', '.join([matrix[i][len(matrix) - 1 - i] for i in range(len(matrix))]) + '.','Sum:', right_sum )



