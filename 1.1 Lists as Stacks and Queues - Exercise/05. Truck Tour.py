from collections import deque

n = int(input())
pumps = deque(input().split() for x in range(n))

for i in range(n):
    fuel = 0
    is_valid = True
    for _ in range(n):
        current = pumps.popleft()
        fuel += int(current[0]) - int(current[1])
        pumps.append(current)
        if fuel < 0:
            is_valid = False
    pumps.append(pumps.popleft())

    if is_valid:
        print(i)
        break



'''
3
1 5
10 3
3 4
---------
1
'''
