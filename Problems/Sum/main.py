# read sums.txt
file = open('sums.txt', 'r')

for i in file:
    a, b = i.split()
    print(int(a) + int(b))

file.close()
