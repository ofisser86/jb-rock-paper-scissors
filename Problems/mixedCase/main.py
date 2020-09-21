mixed = input().split()
print(''.join([mixed[0]] + [mixed[i].title() for i in range(0, len(mixed)) if i > 0]))
