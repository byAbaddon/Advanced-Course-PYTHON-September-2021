bunker_dict = {items : {} for items in input().split(', ')}
for _ in range(int(input())):
    item, product, params = input().split(' - ')
    quan, qual = [ int(x[x.index(':') + 1:]) for x in params.split(';')]
    bunker_dict[item][product] = (quan, qual)
   

print('Count of items:', sum([sum(x[0] for x in tuple(v.values())) for k, v in bunker_dict.items()]))
print(f'Average quality: {sum([sum(x[1] for x in tuple(v.values())) for k, v in bunker_dict.items()]) / len(bunker_dict):.2f}')
[print(f'{items} -> { ", ".join([x for x in bunker_dict[items].keys()])}') for items in bunker_dict]



#--------------------------------------------------------------------(2)-------------------------------------------------

bunker_dict = {items : {} for items in input().split(', ')}
quantity , quality = 0, 0

for _ in range(int(input())):
    item, product, params = input().split(' - ')
    quan, qual = [ int(x[x.index(':') + 1:]) for x in params.split(';')]
    bunker_dict[item][product] = ()
    quantity += quan    
    quality += qual    
   

print(f'Count of items: {quantity}\nAverage quality: {quality / len(bunker_dict):.2f}')
[print(f'{k} -> { ", ".join([x  for x in v.keys()])}') for k, v in bunker_dict.items()]