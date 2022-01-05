from collections import deque

chocolate_list, milk_list = [deque(map(int, input().split(', '))) for _ in range(2)]
milkshakes = 0

while True:
    if not chocolate_list or not milk_list or milkshakes == 5:
        break

    choco = chocolate_list.pop()
    milk = milk_list.popleft()

    if choco == milk:
        milkshakes += 1
    else:
        if choco <= 0:
            milk_list.appendleft(milk)
            continue
        if milk <= 0:
            chocolate_list.append(choco)
            continue
        milk_list.append(milk)
        choco -= 5
        chocolate_list.append(choco)

if milkshakes < 5:
    print('Not enough milkshakes.')
else:
    print('Great! You made all the chocolate milkshakes needed!')

if chocolate_list:
    print(f'Chocolate: {", ".join(map(str, chocolate_list))}')
else:
    print('Chocolate: empty')

if milk_list:
    print(f'Milk: {", ".join(map(str, milk_list))}')
else:
    print('Milk: empty')


'''
20, 24, -5, 17, 22, 60, 26
26, 60, 22, 17, 24, 10, 55
-------------------------
Great! You made all the chocolate milkshakes needed!
Chocolate: 20
Milk: 10, 55
'''
