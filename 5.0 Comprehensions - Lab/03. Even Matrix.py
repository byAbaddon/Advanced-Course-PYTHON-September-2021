print([ [int(x) for x in input().split(', ') if not int(x) & 1]  for _ in range(int(input()))])
