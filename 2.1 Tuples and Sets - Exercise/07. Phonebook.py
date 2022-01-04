phone_dict = {}
while True:
    name, *args = input().split('-')
    if not name.isdigit():
        phone_dict[name] = args
    else:
        for _ in range(int(name)):
            name = input()
            if not name:
                exit()
            elif name not in phone_dict:
                print(f'Contact {name} does not exist.')
            else:
                print(name, '->', *phone_dict[name])
        break

# ----------------------------------(2)--------------------

# phone_dict = {}
#
# while True:
#     token = input().split('-')
#     if len(token) == 2:
#         name, phone = token[0], token[1]
#         if name not in phone_dict:
#             phone_dict[name] = ''
#         phone_dict[name] = phone
#     else:
#         loop = int(token[0])
#         for _ in range(loop):
#             name = input()
#             if name not in phone_dict:
#                 print(f'Contact {name} does not exist.')
#             else:
#                 print(name, '->', phone_dict[name])
#         break

# -------------------------Fucking Judge--------------------------
# phone_dict = {}
# while True:
#     try:
#         name, phone = input().split('-')
#         phone_dict[name] = phone
#     except:
#         while True:
#             name = input()
#             if name == '':
#                 exit()
#             elif name not in phone_dict:
#                 print(f'Contact {name} does not exist.')
#             else:
#                 print(name, '->', phone_dict[name])

'''
Adam-+359888001122
Ralf-666
George-5559393
Silvester-02/987665544
4
Silvester
silvester
Rolf
Ralf
------------------otupt:

Silvester -> 02/987665544
Contact silvester does not exist.
Contact Rolf does not exist.
Ralf -> 666
'''
