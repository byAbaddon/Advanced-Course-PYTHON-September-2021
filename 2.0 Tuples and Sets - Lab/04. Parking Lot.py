n = int(input())
parking_list = set()

for _ in range(n):
    status, number = input().split(', ')
    if status == 'IN':
        parking_list.add(number)
    else:
        parking_list.remove(number)

if not parking_list:
    print('Parking Lot is Empty')
else:    
    for car in parking_list:
        print(car)

'''
4
IN, CA2844AA
IN, CA1234TA
OUT, CA2844AA
OUT, CA1234TA
-----------------output:
Parking Lot is Empty
'''