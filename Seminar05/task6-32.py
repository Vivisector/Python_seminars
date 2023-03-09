#task32
import random

'''
# короткий вариант
li = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
mli = []
mrange = [5,15]
for i in range(len(li)):
    if mrange[0]<li[i]<mrange[1]: mli.append(i)
print(f"элементы, находящиеся в диапазоне от {mrange[0]} до {mrange[1]} находятся на следующих позициях:\n{mli}")
'''

N = int(input('введите размер массива: '))
mi = int(input('нижний диапазон: '))
ma = int(input('верхний диапазон: '))
li=[] #автосборка массива
for i in range(N): 
    li.append(random.randint(-10, 40))
print(f'исходный массив:\n{li}')
# li = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
ml = []
mn = []
mrange = [mi,ma]
d = {}
for i in range(len(li)):
    if mrange[0]<li[i]<mrange[1]:
        ml.append(i)
        mn.append(li[i])
        d[i]=li[i]

print(f'в диапазон от {mrange[0]} до {mrange[1]} попадают элементы на позициях')
print(*ml)
print('для сверки («позиция»: «значение»)')
print(d)
