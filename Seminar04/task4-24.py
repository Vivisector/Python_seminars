# task24
import random
N = 12  # размер массива
mylist = []
for i in range(N):  # заполнение
    mylist.append(random.randint(1, 20))
print("дан массив:")
print(*mylist)
print("суммы «соседей»")
sum = max = pos = 0
for i in range(len(mylist)-2):
    sum = sum+mylist[i]+mylist[i+1]+mylist[i+2]
    if sum > max:
        max = sum
        pos = i
    print(f"{i+1}-{i+3}:{sum}", end=' ')
    sum = 0
print(
    f"\nмаксимум в тройке «соседей» равен {max}, и находится на {pos+2}-й позиции")
