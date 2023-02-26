#task 16
# сколько раз встречается некоторое число FIND в массиве A
import random
LEN = 100
#n = [1,2,3,4,5,5,6,7] # учебный массив
mlist = [] #большой массив (заполним автоматом)
for i in range(0,LEN):
    x=random.randint(0,50)
    mlist.append(x)

FIND = 22 #что ищем
cnt = 0 #сколько раз нашли
for i in range(len(mlist)):
    if mlist[i] == FIND: cnt +=1
print(f"Предложенное число \"{FIND}\" встречается списке из {len(mlist)} случайных элементов {mlist}\n {cnt} раз")