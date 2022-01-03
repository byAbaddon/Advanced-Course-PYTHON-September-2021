green_light, yellow_light = int(input()), int(input())
total_time = green_light + yellow_light
passed_cars = 0
waiting_cars_list = []

for car in [x for x in iter(input, 'END')]:
    current_time = 0
    if car != 'green':
        waiting_cars_list.append(car)
    else:
        while waiting_cars_list and green_light > current_time:
            passed_cars += 1
            waiting_car = waiting_cars_list.pop(0)
            for char in waiting_car:
                current_time += 1
                if current_time > total_time:
                    print(f'A crash happened!\n{waiting_car} was hit at {char}.')
                    exit()

print(f'Everyone is safe.\n{passed_cars} total cars passed the crossroads.')


# --------------------------------(2)------------------------------------
#
# from collections import deque
#
# green_duration = int(input())
# free_window_duration = int(input())
# needed_passing_time = green_duration + free_window_duration
# waiting_cars = deque()
# total_passed_cars = 0
#
# command = input()
# while not command == "END":
#     curr_passing_time = 0
#
#     if command == "green":
#         while waiting_cars and green_duration > curr_passing_time:
#             car = waiting_cars[0]
#             for char in car:
#                 curr_passing_time += 1
#                 if curr_passing_time > needed_passing_time:
#                     print("A crash happened!")
#                     print(f"{car} was hit at {char}.")
#                     exit()
#             total_passed_cars += 1
#             waiting_cars.popleft()
#
#     else:
#         waiting_cars.append(command)
#
#     command = input()
# else:
#     print("Everyone is safe.")
#     print(f"{total_passed_cars} total cars passed the crossroads.")


'''
10
5
Mercedes
green
Mercedes
BMW
Skoda
green
END
---------------
Everyone is safe.
3 total cars passed the crossroads.
'''
