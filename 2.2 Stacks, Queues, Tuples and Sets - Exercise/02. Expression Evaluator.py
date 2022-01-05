from math import floor

data = input().split()
current_list = []
for x in data:
    if x not in ['-', '+', '*', '/']:
        current_list.append(x)
    else:
        index = data.index(x)
        for i in range(len(current_list) + len(current_list) // 2):
            if i & 1:
                current_list.insert(i, data[index])
        current_list = [str(floor(eval(' '.join(current_list))))]

print(current_list[0])


'''
6 3 - 2 1 * 5 /

-----
1
'''
