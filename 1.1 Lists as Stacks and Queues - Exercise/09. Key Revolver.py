bullet_price, gun_size, bullets_list, locks_list, intelligence = \
    [list(map(int, input().split())) for x in range(5)]

reload = 0
while bullets_list and locks_list:
    bullet = bullets_list.pop()

    if bullet > locks_list[0]:
        print('Ping!')
    else:
        print('Bang!')
        locks_list.pop(0)

    reload += 1
    if reload % gun_size[0] == 0 and bullets_list:
        print('Reloading!')

if not locks_list:
    print(f"{len(bullets_list)} bullets left. Earned ${intelligence[0] - (reload * bullet_price[0])}")
else:
    print(f"Couldn't get through. Locks left: {len(locks_list)}")

'''
50
2
11 10 5 11 10 20
15 13 16
1500
-------------
Ping!
Bang!
Reloading!
Bang!
Bang!
Reloading!
2 bullets left. Earned $1300

'''
