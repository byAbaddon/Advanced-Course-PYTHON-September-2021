strings_list = input().split()

colors_list = ['red', 'yellow', 'blue']
secondary_colors_list = ['orange', 'purple', 'green']
result_list = []
is_last = False

while strings_list:
    right = ''
    left = strings_list.pop(0)
    if strings_list:
        right = strings_list.pop()
    else:
        is_last = True

    color = left + right
    color_two = right + left

    if color in colors_list or color in secondary_colors_list:
        color = color
    elif color_two in colors_list or color_two in secondary_colors_list:
        color = color_two

    if color in colors_list or color in secondary_colors_list:
        result_list.append(color)
    elif is_last:
        break
    else:
        position = 0
        if len(left) != 1:
            left = left[0:-1]
            if len(strings_list) & 1:
                position = 1
            strings_list.insert(len(strings_list) // 2 + position, left)
        if len(right) != 1:
            right = right[0:-1]
            strings_list.insert(len(strings_list) // 2 + position, right)

for color in result_list:
    if color in secondary_colors_list:
        if color == 'orange':
            if 'red' not in result_list or 'yellow' not in result_list:
                result_list.remove(color)
        if color == 'purple':
            if 'red' not in result_list or 'blue' not in result_list:
                result_list.remove(color)
        if color == 'green':
            if 'yellow' not in result_list or 'blue' not in result_list:
                result_list.remove(color)


print(result_list)

'''
r ue nge ora bl ed
-----------------
['red', 'blue']
'''
