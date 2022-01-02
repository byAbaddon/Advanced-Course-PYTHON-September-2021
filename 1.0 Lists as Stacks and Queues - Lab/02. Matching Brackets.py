expression = input()
stack = []

for i in range(len(expression)):
    if expression[i] == '(':
        stack.append(i)

    if expression[i] == ')':
        start_index = stack.pop()
        end_index = i
        print(expression[start_index: end_index + 1])

'''
1 + (2 - (2 + 3) * 4 / (3 + 1)) * 5

------------
(2 + 3)
(3 + 1)
(2 - (2 + 3) * 4 / (3 + 1))
'''