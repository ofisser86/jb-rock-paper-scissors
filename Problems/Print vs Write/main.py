numbers = [1234, 5678, 90]
# save this list in `file_with_list.txt`
f = open('file_with_list.txt', 'w')
print(numbers, file=f, end='')

f.close()
