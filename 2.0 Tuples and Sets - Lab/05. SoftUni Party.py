guests_list = [input() for _ in range(int(input()))]
vip_list = []

while True:
    guest = input()
    if guest == 'END':
        print(len(guests_list))
        break
    else:
        if guest in guests_list:
            guests_list.remove(guest)

for guest in guests_list:
    if guest[0].isdigit():
        vip_list.append(guest)
        guests_list.remove(guest)

sorted_vip_list = sorted(vip_list)
for vip in sorted_vip_list:
    print(vip)

sorted_guests_list = sorted(guests_list)
for ordinary in sorted_guests_list:
    print(ordinary)

'''
5
7IK9Yo0h
9NoBUajQ
Ce8vwPmE
SVQXQCbc
tSzE5t0p
9NoBUajQ
Ce8vwPmE
SVQXQCbc
END
------------output:
2
7IK9Yo0h
tSzE5t0p
'''