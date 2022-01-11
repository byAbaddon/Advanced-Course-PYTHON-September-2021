print([n for n in range( int(input()), int(input()) + 1)  if  any([n % x == 0 for x in range(2, 11)])])
