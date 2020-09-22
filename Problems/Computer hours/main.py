# Make sure your output matches the assignment *exactly*
question = int(input())

if question < 2:
    print('That seems reasonable')
elif 2 <= question < 4:
    print('Do you have time for anything else?')
else:
    print('You need to get outside more!')
