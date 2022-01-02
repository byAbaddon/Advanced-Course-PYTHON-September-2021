water = int(input())
people_list = [x for x in iter(input, 'Start')]

while True:
    com, *args = input().split()

    if com == 'End':
        print(f'{water} liters left')
        break
    elif com == 'refill':
        water += int(args[0])
    else:
        liters = int(com)
        if water >= liters:
            water -= liters
            print(f'{people_list.pop(0)} got water')
        else:
            people = people_list.pop(0)
            people_list.append(people)
            print(f'{people} must wait')

# ----------------------------------(2)---------------------

# water = int(input())
# people = []
#
# while True:
#     token = input()
#     if token == 'Start':
#         break
#     people.append(token)
#
# while True:
#     token = input().split()
#     if token[0] == 'End':
#         print(f'{water} liters left')
#         break
#     elif token[0] == 'refill':
#         water += int(token[1])
#     else:
#         person_name = people.pop(0)
#         if water >= int(token[0]):
#             water -= int(token[0])
#             print(f'{person_name} got water')
#         else:
#             print(f'{person_name} must wait')


'''
2
Peter
Amy
Start
2
refill 1
1
End
----------------

Peter got water
Amy got water
0 liters left


'''
