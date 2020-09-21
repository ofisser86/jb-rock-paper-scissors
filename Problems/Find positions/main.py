# put your python code here
numbers = [int(i) for i in input().split()]
num = int(input())
indexes = []
if num in numbers:
    for i in enumerate(numbers):
        if i[1] == num:
            indexes.append(str(i[0]))
else:
    print('not found')

print(' '.join(indexes))
