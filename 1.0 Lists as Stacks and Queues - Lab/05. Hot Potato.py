people_list, n = input().split(), int(input())

while len(people_list) > 1:
    for i in range(1, n):
        people_list.append(people_list.pop(0))
    else:
        print('Removed', people_list.pop(0))

print('Last is', *people_list)

'''
George Peter Michael William Thomas
10
------------
Removed Emily
Removed Tracy
Last is Daniel
'''
