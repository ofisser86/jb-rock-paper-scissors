dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']
sen = input().split()
ok = True
for i in sen:
    if i not in dictionary:
        print(i)
        ok = False

if ok:
    print('OK')
# missed = [word for word in input().split() if word not in dictionary]
# print("\n".join(missed) or "OK")