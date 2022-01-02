names_list = []

while True:
    token = input()
    if token == 'End':
        print(f'{len(names_list)} people remaining.')
        break
    elif token == 'Paid':
        for _ in range(len(names_list)):
            print(names_list.pop(0))
    else:
        names_list.append(token)


'''
Anna
Emma
Alexander
End
------------------

3 people remaining.
'''