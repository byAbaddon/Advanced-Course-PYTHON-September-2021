tuple_list = list(zip([x for x in input().split(', ')], [x for x in input().split(', ')]))
[print(' -> '.join(x))  for x in tuple_list]


