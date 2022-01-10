def even_odd(*args):
    com = args[-1]
    if com == 'even':
        return [x for x in args[: -1] if not int(x) & 1]
    else:
        return [x for x in args[: -1] if int(x) & 1]


'''
print(even_odd(1, 2, 3, 4, 5, 6, "even"))
----------
[2, 4, 6]
'''