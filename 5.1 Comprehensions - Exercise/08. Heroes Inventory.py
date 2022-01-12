heros_dict = {name : {} for name in input().split(', ')}

while True:
    try:
        name, item, cost = [int(x) if x.isdigit() else x for x in input().split('-')]
        if item not in heros_dict[name]:
            heros_dict[name][item] = cost
    except:
        [print(f'{k} -> Items: {len(v)}, Cost: {sum(v.values())}') for k, v in heros_dict.items()]
        break


