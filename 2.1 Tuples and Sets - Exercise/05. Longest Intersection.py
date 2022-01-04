loop = int(input())
intersection_list = []

for _ in range(loop):
    first_range, second_range = input().split('-')
    first = {x for x in range(int(first_range.split(',')[0]), int(first_range.split(',')[1]) + 1)}
    second = {x for x in range(int(second_range.split(',')[0]), int(second_range.split(',')[1]) + 1)}
    intersection = first.intersection(second)
    intersection_list.append(intersection)

intersection_list = sorted(intersection_list, key=lambda el: -len(el))
print(f'Longest intersection is {list(intersection_list[0])} with length {len(intersection_list[0])}')


'''
3
0,3-1,2
2,10-3,5
6,15-3,10
------------
Longest intersection is [6, 7, 8, 9, 10] with length 5
'''