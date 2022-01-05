materials_list, magic_list = [list(map(int, input().split())) for x in range(2)]
factory_dict = {150: 'Doll', 250: 'Wooden train', 300: 'Teddy bear', 400: 'Bicycle'}
presents_dict = {}

while materials_list and magic_list:
    material = materials_list.pop()
    magic = magic_list.pop(0)
    current_result = material * magic

    if current_result in factory_dict:
        present = factory_dict[current_result]
        if present not in presents_dict:
            presents_dict[present] = 0
        presents_dict[present] += 1
    elif current_result < 0:
        materials_list.append(material + magic)
    elif current_result > 0:
        materials_list.append(material + 15)
    elif current_result == 0:
        if material != 0:
            materials_list.append(material)
        if magic != 0:
            magic_list.insert(0, magic)


if 'Doll' in presents_dict and 'Wooden train' in presents_dict or\
        'Teddy bear' in presents_dict and 'Bicycle' in presents_dict:
    print('The presents are crafted! Merry Christmas!')
else:
    print('No presents this Christmas!')
if materials_list:
    print(f'Materials left: {", ".join(map(str, list(materials_list)[::-1]))}')
if magic_list:
    print(f'Magic left: {", ".join(str(x) for x in magic_list)}')
[print(f'{k}: {v}') for k, v in sorted(presents_dict.items())]


'''
10 -5 20 15 -30 10
40 60 10 4 10 0
----------------------------
The presents are crafted! Merry Christmas!
Materials left: 20, -5, 10
Bicycle: 1
Teddy bear: 2
'''