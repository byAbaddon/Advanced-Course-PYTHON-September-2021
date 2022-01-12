matrix = [ [int(x) for  x in input().split()]  for x in range(int(input()))]

while True:
    try:
        command, row, col, val = [ int(x) if x.isdigit() else x for x in input().split()]

        if command == 'Add':
            try:
                matrix[row][col] += val      
            except:
                print('Invalid coordinates')
        else:
            try:
                matrix[row][col] -= val      
            except:
                print('Invalid coordinates')       

    except:
        [print(*x) for x in matrix]
        break


