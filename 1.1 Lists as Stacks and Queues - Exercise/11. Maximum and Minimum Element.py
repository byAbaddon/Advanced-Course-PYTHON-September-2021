loop = int(input())
stack = []

for _ in range(loop):
    token = list(map(int, input().split()))
    if token[0] == 1:
        stack.append(token[1])
    elif token[0] == 2 and len(stack) > 0:
        stack.pop()
    elif token[0] == 3 and len(stack) > 0:
        print(max(stack))
    elif token[0] == 4 and len(stack) > 0 :
        print(min(stack))

print(', '.join(map(str ,list(reversed(stack)))))     