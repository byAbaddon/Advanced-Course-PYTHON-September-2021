quantity = int(input())
clients_list = [int(x) for x in input().split()]

print(max(clients_list))

while clients_list:
    if quantity >= clients_list[0]:
        quantity -= clients_list.pop(0)
    else:
        print('Orders left:', *clients_list)
        exit()

print('Orders complete')


'''
348
20 54 30 16 7 9
--------------------
54
Orders complete
'''