string = input().split()
ends_with_s = []
for i in string:
    if i.endswith('s'):
        ends_with_s.append(i)
print('_'.join(ends_with_s))
