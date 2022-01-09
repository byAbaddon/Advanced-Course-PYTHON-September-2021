import os
os.system('clear')

def rounded(num):
    return list(map( int, filter(lambda x: not int(x) & 1 , num.split())))

def even_num(num):
    return list(map( int, filter(lambda x: not int(x) & 1 , num.split())))

print(even_num(input()))   