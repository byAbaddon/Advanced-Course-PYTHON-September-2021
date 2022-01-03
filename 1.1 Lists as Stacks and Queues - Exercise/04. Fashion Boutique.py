clothes = [int(x) for x in input().split()]
rack = int(input())
num_racks, current = 0, 0

while clothes:
    out = clothes.pop(0)
    current += out
    if rack == current:
        num_racks += 1
        current = 0
        continue
    elif rack < current:
        num_racks += 1
        clothes.insert(0, out)
        current = 0
        continue

    if len(clothes) == 0:
        num_racks += 1

print(num_racks)

'''
5 4 8 6 3 8 7 7 9
16
------
5
'''