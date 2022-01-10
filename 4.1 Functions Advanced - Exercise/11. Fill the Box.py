def fill_the_box(*args):
    h, l, w = args[0:3]
    box = h * l * w
    box_list = list(args[3:])
    while box_list:
        current_box = box_list.pop(0)
        if current_box == 'Finish':
            break
        box -= current_box
        if box <= 0:
            return f'No more free space! You have {abs(box) + sum([x for x in box_list if x != "Finish"])} more cubes.'
    return f'There is free space in the box. You could put {box} more cubes.'


'''
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
------------------------
No more free space! You have 17 more cubes.
'''
