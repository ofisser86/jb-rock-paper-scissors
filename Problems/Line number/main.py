# read sample.txt and print the number of lines
file = open('sample.txt', 'r')
count = 0
for _ in file:
    count += 1
print(count)
file.close()