bees_list, nectar_list, symbols_list = \
    [list(map(lambda x: int(x) if x.isdigit() else x, input().split())) for _ in range(3)]
total_nectar = 0

while bees_list and nectar_list:
    bee = bees_list.pop(0)
    nectar = nectar_list.pop()

    if nectar >= bee:
        symbol = symbols_list.pop(0)
        if symbol == '/' and bee == 0 and nectar == 0:
            continue
        total_nectar += abs(eval(f'{bee} {symbol} {nectar}'))
    else:
        bees_list.insert(0, bee)


print('Total honey made:', total_nectar)
if bees_list:
    print(f'Bees left: {", ".join(map(str, bees_list))}')
if nectar_list:
    print(f'Nectar left: {", ".join(map(str, nectar_list))}')


'''
0 62 99 35 0 150
120 60 10 1 70 10
/ - + + / * - - /



20 62 99 35 0 150
120 60 10 1 70 10
+ - + + / * - - /
---------------------------output:
Total honey made: 148
Bees left: 99, 35, 0, 150
'''
