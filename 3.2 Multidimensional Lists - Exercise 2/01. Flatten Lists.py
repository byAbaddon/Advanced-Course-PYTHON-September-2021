print(*list(filter(lambda x: x != '', sum([x.split(' ') for x in reversed(input().split('|'))], []))))

# ----------------------------------(2)------------------------
# res = []
# data = input().split('|')
# for row in reversed(data):
#     res += str(row).split(' ')
# res = list(filter(lambda x: x != '', res))
# print(*res)

''' 
1 2 3 |4 5 6 |  7  88
-------------------------
7 88 4 5 6 1 2 3
'''
