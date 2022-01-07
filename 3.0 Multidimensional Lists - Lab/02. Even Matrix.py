print([[int(x) for x in input().split(', ') if not int(x) & 1] for _ in range(int(input()))])


'''
2
1, 2, 3
4, 5, 6
-------------
[[2], [4, 6]]
'''