num_list = input().split()
positive_sum = sum([int(x) for x in num_list if int(x) > 0])
negative_sum = sum([int(x) for x in num_list if int(x) < 0])

print(f'{negative_sum}\n{positive_sum}')

if abs(negative_sum) > positive_sum:
    print('The negatives are stronger than the positives')
else:
    print('The positives are stronger than the negatives')
