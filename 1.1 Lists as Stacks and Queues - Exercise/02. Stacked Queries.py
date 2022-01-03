stack = []

for i in range(int(input())):
    token = input()
    if len(token) > 1:
        stack.append(int(token.split()[1]))
    else:
        if stack:
            if token == '2':
                stack.pop()
            elif token == '3':
                print(max(stack))
            else:
                print(min(stack))

print(*reversed(stack), sep=', ')

'''
9
1 97
2
1 20
2
1 26
1 20
3
1 91
4

----------------
26
20
91, 20, 26

'''