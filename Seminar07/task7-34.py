# task34
# glasnye = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
mYes = '«Парам пам-пам» - ритм сохранен'
mNo = '«Пум пурум» - ритм нарушен'
stroka = ('пара-ра-рам рам-пам-папам па-ра-па-дам').lower()
# stroka = ('пара-ра-рам рам-пам-папам па-ра-па-дам ду-да-да').lower()
print('фраза:', stroka)
slova = stroka.split()

'''
# простое решение
cnt=0
for i in range(len(slova)):
    for j in slova[i]:
        if j in ('ауоыиэяюёе'):
            cnt+=1
print('слов -', len(slova))
print('слогов -', cnt, '\nответ:', end=' ')
if cnt%len(slova)==0:
    print(mYes)
else:
    print(mNo)
'''
'''
# чуть более красивое
# сразу считаем колво слогов в первом слове и сравниваем с остальными
cnt = len(list(_ for _ in stroka.split() if _ in 'ауоыиэяюёе'))
# cnt=len([_ for _ in slova[0] if _ in 'ауоыиэяюёе'])
flag = 1 # ритм есть

for i in range(len(slova)):
    if (len([_ for _ in slova[i] if _ in 'ауоыиэяюёе'])!=cnt):
        flag=0
        break

if flag==0:
    print(mNo)
else:
    print(mYes)
'''
# самое короткое решение
if (len(list(_ for _ in stroka if _ in 'ауоыиэяюёе')))%len(slova)==0:
    print(mYes)
else:
    print(mNo)
