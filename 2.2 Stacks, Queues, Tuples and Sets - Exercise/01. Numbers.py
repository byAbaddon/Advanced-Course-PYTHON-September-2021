f_list, s_list = [set(map(int, input().split())) for _ in range(2)]

for _ in range(int(input())):
    com, pos, *args = list(map(lambda x: int(x) if x.isdigit() else x, input().split()))
    nums = set(args)
    if com == 'Add':
        if pos == 'First':
            f_list |= nums
        else:
            s_list |= nums
    if com == 'Remove':
        if pos == 'First':
            f_list -= nums
        else:
            s_list -= nums
    if com == 'Check':
        print(s_list < f_list)

print(*sorted(f_list), sep=', ')
print(*sorted(s_list), sep=', ')


'''
1 2 3 4 5
1 2 3
3
Add First 5 6
Remove Second 8 9 11
Check Subset

--------------------
True
1, 2, 3, 4, 5, 6
1, 2, 3

'''