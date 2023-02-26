# task14
# Задача 14: Требуется вывести все целые степени двойки (т.е. числа
# вида 2k), не превосходящие числа N.
N = 2100
tmp = 2 #множитель
for i in range(N):
    tmp = tmp*2
    if tmp<N:
        print(tmp)
    else:
        break