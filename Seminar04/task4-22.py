#task 22
import random
n = int(input('Введите размер первого набора чисел: '))
m = int(input('Введите размер второго набора чисел: '))
print('Первый набор:')
n_list = []
for i in range(n):
    # n_list.append(int(input(f'{i+1}-е число из {n}-ти: ')))
    n_list.append(random.randint(1,20))

print('\nВторой набор:')
m_list = []
for i in range(m):
    # m_list.append(int(input(f'{i+1}-е число из {m}-ти: ')))
    m_list.append(random.randint(1,20))

print(f"первый набор:\n{n_list}")
print(f"второй набор:\n{m_list}")
print(f"общие числа из обоих наборов: {sorted(set(n_list).intersection(set(m_list)))}")