numbers_list = input().split(', ')
print(f'Positive: {", ".join([x for x in numbers_list if int(x) >= 0])}')
print(f'Negative: {", ".join([x for x in numbers_list if int(x) < 0])}')
print(f'Even: {", ".join([x for x in numbers_list if not int(x) & 1 ])}')
print(f'Odd: {", ".join([x for x in numbers_list if int(x) & 1])}')



