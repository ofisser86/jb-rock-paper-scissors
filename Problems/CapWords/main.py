class_name = input()
tmp = ''
for i in class_name:
    if i in ('-', '_'):
        tmp += ' '
        continue
    tmp += i

res = [i.capitalize() for i in tmp.split()]

print(''.join(res))
