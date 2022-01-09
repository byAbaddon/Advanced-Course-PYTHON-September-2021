from itertools import permutations

data = input()
[print(''.join(x)) for x in permutations(data, len(data))]

'''
abc
-----------------------------
abc
acb
bac
bca
cab
cba
'''

# ---------------------------------------------

# def combination(string, index):   #----------copy /paste 100pts
#     if index >= len(string):
#         print(''.join(string))
#         return
#
#     combination(string ,index+1)
#
#     for i in range(index + 1, len(string)):
#         string[index], string[i] = string[i], string[index]
#         combination(string, index + 1)
#         string[index], string[i] = string[i], string[index]
#
#
# combination(list(input()), 0)