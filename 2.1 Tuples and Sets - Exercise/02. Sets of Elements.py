n, m = input().split()
one_set = {input() for _ in range(int(n))}
two_set = {input() for _ in range(int(m))}
[print(x) for x in one_set.intersection(two_set)]

'''
4 3
1
3
5
7
3
4
5
------
3
5
'''
