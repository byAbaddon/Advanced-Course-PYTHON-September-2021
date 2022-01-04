text = input()
chars_dict = {}

for char in text:
    if char not in chars_dict:
        chars_dict[char] = 0
    chars_dict[char] += 1

[print(f'{k}: {v} time/s') for k, v in sorted(chars_dict.items())]

'''
SoftUni rocks
----------------
 : 1 time/s
S: 1 time/s
U: 1 time/s
c: 1 time/s
f: 1 time/s
i: 1 time/s
k: 1 time/s
n: 1 time/s
o: 2 time/s
r: 1 time/s
s: 1 time/s
t: 1 time/s
'''
