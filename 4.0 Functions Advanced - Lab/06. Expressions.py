def expression(n, res=0, exp=''):
    if n:
        plus_r = expression(n[1:], res + n[0], f'{exp}+{n[0]}')
        min_r = expression(n[1:], res + n[0], f'{exp}-{n[0]}')
        return plus_r + min_r
    return [exp]


data = list(map(int, input().split(', ')))
[print(f'{e}={eval(e)}') for e in expression(data)]

'''
1, 2
-----------------
+1+2=3
+1-2=-1
-1+2=1
-1-2=-3

'''
