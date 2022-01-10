command, num_list = input(), input().split()

if command == 'Even':
    print(sum([int(x) for x in num_list if not int(x) & 1]) * len(num_list))
else:
    print(sum([int(x) for x in num_list if int(x) & 1]) * len(num_list))

'''
Odd
1 3 5 34 7 9 12 11 13 10
------------
490
'''
