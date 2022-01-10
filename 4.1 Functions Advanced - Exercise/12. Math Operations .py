def math_operations(*args, **kwargs):
    args = list(args)
    while args:
        for k, v in kwargs.items():
            if not args:
                break
            if k == 'a':
                kwargs[k] += args.pop(0)
            if k == 's':
                kwargs[k] -= args.pop(0)
            if k == 'd':
                el = args.pop(0)
                if el != 0:
                    kwargs[k] /= el
            if k == 'm':
                kwargs[k] *= args.pop(0)
    return kwargs


'''
print(math_operations(2, 12, 0, -3, 6, -20, -11, a=1, s=7, d=33, m=15))
-------------------
{'a': 9, 's': 15, 'd': -3.0, 'm': -45}
'''

