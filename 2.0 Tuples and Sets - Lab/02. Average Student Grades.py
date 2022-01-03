students_list = [input().split() for x in range(int(input()))]
students_dict = {}
for student in students_list:
    name, grade = student
    if name not in students_dict:
        students_dict[name] = []
    students_dict[name].append(float(grade))

for k, v in students_dict.items():
    print(f'{k} ->', *[f'{x:.2f}' for x in v], f'(avg: {sum(v) / len(v):.2f})')

# ------------------------------------(2)-----------------------
# loop = int(input())
# student_dict = {}
# string = ''
#
# for _ in range(loop):
#     token = input().split()
#     key, val = token[0], float(token[1])
#     if key not in student_dict:
#         student_dict[key] = []
#     student_dict[key].append(val)
#
# for key, val in student_dict.items():
#     for v in val:
#         string += f'{v:.2f} '
#     print(f'{key} -> {string}(avg: {sum(val) / len(val):.2f})')
#     string = ''

'''
4
Scott 4.50
Ted 3.00
Scott 5.00
Ted 3.66
----------------------
Ted -> 3.00 3.66 (avg: 3.33)
Scott -> 4.50 5.00 (avg: 4.75)
'''
