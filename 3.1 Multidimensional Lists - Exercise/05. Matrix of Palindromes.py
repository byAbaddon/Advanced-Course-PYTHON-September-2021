row, col = list(map(int, input().split()))

for i in range(row):
    for j in range(col):
        print(chr(97 + i) + chr(97 + i + j) + chr(97 + i), end=' ')
    print(' ')


'''
4 6
-------------
aaa aba aca ada aea afa
bbb bcb bdb beb bfb bgb
ccc cdc cec cfc cgc chc
ddd ded dfd dgd dhd did
'''