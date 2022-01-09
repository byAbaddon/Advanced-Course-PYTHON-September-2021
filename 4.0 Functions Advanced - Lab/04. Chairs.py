from itertools import combinations

[print(*x, sep=', ') for x in list(combinations(input().split(', '), int(input())))]

# --------------------------------------(2)-----------------------------

# collection = []
#
#
# def combination(names, loop):
#
#     if len(collection) == loop:
#         print(', '.join(collection))
#         return
#     for i in range(len(names)):
#         collection.append(names[i])
#         combination(names[i + 1:], loop)
#         collection.pop()
#
#
# combination(input().split(', '), int(input()))

'''
Peter, George, Amy
2
-----------------------
Peter, George
Peter, Amy
George, Amy
'''