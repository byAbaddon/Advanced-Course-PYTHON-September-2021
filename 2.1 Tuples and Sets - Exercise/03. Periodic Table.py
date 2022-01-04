print(*set(sum([input().split() for _ in range(int(input()))], [])), sep='\n')

# ------------------------------(2)-------------
# n = int(input())
# element_set = set()
#
# while n:
#     n -= 1
#     for el in input().split():
#         element_set.add(el)
#
# for el in element_set:
#     print(el)

'''
4
Ce O
Mo O Ce
Ee
Mo
------------
Ce
Ee
Mo
O
'''
