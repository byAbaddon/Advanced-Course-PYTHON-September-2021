cups_list, bottle_list = [list(map(int, input().split())) for x in range(2)]
wasted_water = 0

while cups_list and bottle_list:
    cup = cups_list[0]
    bottle = bottle_list.pop()

    if cup > bottle:
        while cup > 0:
            if bottle < cup:
                cup -= bottle
                bottle = bottle_list.pop()
            else:
                bottle -= cup
                cup = 0
    wasted_water += abs(bottle - cup)
    cup = cups_list.pop(0)

if cups_list:
    print('Cups:', *cups_list, f'\nWasted litters of water: {wasted_water}')
else:
    print(f'Bottles:', *bottle_list, f'\nWasted litters of water: {wasted_water}')


# -----------------------------(2)---------------------------------------
# cups = [int(x) for x in input().split()]
# bottles = list(reversed([int(x) for x in input().split()]))
#
# water = 0
#
# while True:
#     for i in range(10):
#         try:
#             if cups[i] <= bottles[i]:
#                 if cups[i] < bottles[i]:
#                     water += abs(cups[i] - bottles[i])
#                     cups.pop(i)
#                     bottles.pop(i)
#                     break
#                 else:
#                     cups.pop(i)
#                     bottles.pop(i)
#                     break
#             elif cups[i] > bottles[i]:
#                 cups[i] -= bottles[i]
#                 bottles.pop(i)
#                 break
#         except:
#             if cups:
#                 print('Cups:', *cups)
#             else:
#                 print('Bottles:', *bottles)
#
#             print(f'Wasted litters of water: {water}')
#             exit()


'''
10 20 30 40 50
20 11
----------------
Cups: 30 40 50
Wasted litters of water: 1
'''