from itertools import chain


def operate(operator, *args):
    return eval(''.join([str(x) for x in chain(*[*zip(args, (operator * (len(args))))])][:-1]))
# -------------------------------------------------(2)------------------
# def operate(operator, *args):
#     if operator == '*' or operator == '/':
#         result = 1
#     else:
#         result = 0
#     for element in args:
#         if operator == '+':
#             result += element
#         elif operator == '*':
#             result *= element
#         elif operator == '-':
#             result -= element
#         elif operator == '/':
#             result /= element
#
#     return result

print(operate('+', 1, 2, 3))
print(operate("/", 12, 4))
'''

----
6

'''
