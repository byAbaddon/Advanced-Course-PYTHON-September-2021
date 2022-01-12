result_dict = {x : len(x) for x in input().split(', ')}
print(", ".join([f'{k} -> {v}'  for k,v in result_dict.items()]))