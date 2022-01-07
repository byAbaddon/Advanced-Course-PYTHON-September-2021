rows, cols = [int(x) for x in input().split()]
text = input() * 30
matrix = []
start = 0

for i in range(rows):
    if not i & 1:
        matrix.append(text[start: start + cols])
        start += cols
    else:
        reverse = text[start: start + cols]
        start += cols
        matrix.append(reverse[::-1])

print(*matrix, sep='\n')




'''
1 4
Python
-----------
Pyth
'''
