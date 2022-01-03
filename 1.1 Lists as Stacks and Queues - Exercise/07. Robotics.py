from collections import deque


def next_second(h, m, s):
    s += 1
    if s == 60:
        m += 1
        s = 0
    if m == 60:
        h += 1
        m = 0
    if h == 24:
        h = 0

    return h, m, s


robot_info = input().split(";")
time = list(map(int, input().split(":")))
robots_dict = {}
available_robots = deque()
waiting_robots = deque()
products = deque()

product = input()
while not product == "End":
    products.append(product)
    product = input()

for robot in robot_info:
    name, processing_time = robot.split("-")
    processing_time = int(processing_time)
    available_robots.append([name, processing_time])
    robots_dict[name] = processing_time

while products:
    for robot in waiting_robots:
        name = robot[0]
        robot[1] -= 1
        if robot[1] <= 0:
            available_robots.append([name, robots_dict[name]])
    waiting_robots = [robot for robot in waiting_robots if robot[1] > 0]

    time = next_second(time[0], time[1], time[2])
    curr_product = products.popleft()

    if not available_robots:
        products.append(curr_product)
        continue

    curr_robot = available_robots.popleft()
    waiting_robots.append(curr_robot)
    print(f"{curr_robot[0]} - {curr_product} [{time[0]:02d}:{time[1]:02d}:{time[2]:02d}]")


# ---------------------------------FUCK OFF-----------------------------------------------

# from datetime import datetime, timedelta
#
# robot_list = [k for k in [x.split('-') for x in input().split(';')]]
# h, m, s = map(int, input().split(':'))
# items = [x for x in iter(input, 'End')]
#
# working_dict = {}
# add_second = 0
# is_working = True
# current_robot_work_time = 0
#
#
# def get_time():
#     global add_second
#     add_second += 1
#     current_time = datetime(2021, 10, 26, h, m, s)
#     new_time = current_time + timedelta(0, add_second)
#     return new_time.time()
#
#
# for robot in robot_list:
#     item = items.pop(0)
#     robot_name, _ = robot
#     print(f'{robot_name} - {item} [{get_time()}]')
#
# while items:
#     if len(robot_list) > 1:
#         get_time()
#     for robot in robot_list:
#         name, work_time = map(lambda x: int(x) if x.isdigit() else x, robot)
#         if is_working:
#             current_robot_work_time = work_time
#             is_working = False
#         work_time -= 1
#
#         if work_time > 0:
#             if items:
#                 items.append(items.pop(0))
#             robot_list.pop(0)
#             robot_list.append([name, str(work_time)])
#             if len(robot_list) == 1:
#                 get_time()
#         else:
#             is_working = True
#             item = items.pop(0)
#             robot_list.pop(0)
#             robot_list.append([name, str(current_robot_work_time)])
#             print(f'{name} - {item} [{get_time()}]')

'''
ROB-15;SS2-10;NX8000-3
8:00:00
detail
glass
wood
apple
End
-----------------
ROB - detail [08:00:01]
SS2 - glass [08:00:02]
NX8000 - wood [08:00:03]
NX8000 - apple [08:00:06]

'''
