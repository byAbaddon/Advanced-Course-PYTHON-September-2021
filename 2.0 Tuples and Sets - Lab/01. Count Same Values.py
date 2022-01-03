num_list = [float(x) for x in input().split()]
unique_num_list = sorted(set(num_list), key=num_list.index)
[print(f'{n} - {num_list.count(n)} times') for n in unique_num_list]

# -----------------------(2)------------------------

# num_list = [float(x) for x in input().split()]
# count_dict = {}
#
# for n in num_list:
#     if n not in count_dict:
#         count_dict[n] = 0
#     count_dict[n] += 1
#
# for k, v in count_dict.items():
#     print(f'{k} - {v} times')


'''
-2.5 4 3 -2.5 -5.5 4 3 3 -2.5 3
---------------
-2.5 - 3 times
4.0 - 2 times
3.0 - 4 times
-5.5 - 1 times
'''
